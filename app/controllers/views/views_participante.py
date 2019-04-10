from app.controllers.views.imports.vp_dep import *

def cadastro():
    form = CadastroForm(request.form)
    if form.validate_on_submit():
        usuario, salt, token = Usuario.criar_usuario(form)
        enviarEmailConfirmacao(usuario, token)
        login_user(usuario, remember=True)
        return redirect(url_for('verificar_email'))
    return render_template('cadastro.html', form=form)

@login_required
def verificar_email():
    if email_confirmado() == True:
        msg = 'Seu email foi verificado com sucesso!'
        status = True
    else:
        msg = 'Confirme o email de verificação que foi enviado ao endereço de email fornecido'
        status = False
    return render_template('confirma_email.html', resultado=msg, status=status)

@login_required
def cadastro_participante():
    form = ParticipanteForm(request.form)
    if form.validate_on_submit():
        try:
            valida_participante(current_user)
            participante = Participante.cria_participante(form)
            return redirect(url_for('dashboard_usuario'))
        except ParticipanteExiste:
            return render_template('cadastro_participante.html', form=form)
        except EmailNaoConfirmado:
            return redirect(url_for('verificar_email'))
    return render_template('cadastro_participante.html', form=form)

@login_required
def dashboard_usuario():
    usuario = db.session.query(Usuario).filter_by(
        id=current_user.id).first()
    if email_confirmado():
        participante = db.session.query(Participante).filter_by(
            usuario=current_user).first()
        return render_template('dashboard_usuario.html', title='Dashboard', usuario=usuario, participante=participante)
    else:
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        salt = gensalt().decode('utf-8')
        token = serializer.dumps(current_user.email, salt=salt)
        usuario = current_user
        usuario.salt = salt
        usuario.token_email = token
        usuario.email_verificado = False
        db.session.add(usuario)
        db.session.commit()
        enviarEmailConfirmacao(app, usuario.email, token)
        login_user(usuario, remember=True)
        return redirect(url_for('verificar_email'))

@login_required
def envio_comprovante():
    """
    Página de envio de comprovantes de pagamento
    """
    form = ComprovanteForm()
    if form.validate_on_submit():
        comprovante = form.comprovante.data
        filename = secure_filename(comprovante.filename)
        filename = f'{current_user.id}_{current_user.primeiro_nome}_{current_user.sobrenome}_{filename}'
        upload_path = path.join(app.config['UPLOAD_FOLDER'], 'comprovantes')
        if not path.exists(upload_path):
            makedirs(upload_path)
        comprovante.save(path.join(upload_path, filename))
        flash('Comprovante enviado com sucesso!')
        return redirect(url_for('dashboard_usuario'))
    return render_template('enviar_comprovante.html', form=form)

def verificacao(token):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        # Acha o usuário que possui o token
        user = db.session.query(Usuario).filter_by(token_email=token).first()
        salt = user.salt
        # Gera um email a partir do token do link e do salt do db
        email = serializer.loads(token, salt=salt, max_age=3600)
        user.email = email
        # Valida o email
        user.email_verificado = True
        db.session.add(user)
        db.session.commit()
    # Tempo definido no max_age
    except SignatureExpired:
        return render_template('cadastro.html', resultado='O link de ativação expirou.')
    except Exception as e:
        print(e)
        return render_template('cadastro.html', resultado='Falha na ativação.')
    return redirect(url_for('verificar_email'))


@login_required
def inscricao_atividades():
    minicursos = db.session.query(Atividade).filter_by(
        tipo=TipoAtividade['minicurso'])
    workshops = db.session.query(Atividade).filter_by(
        tipo=TipoAtividade['workshop'])
    palestras = db.session.query(Atividade).filter_by(
        tipo=TipoAtividade['palestra'])
    return render_template('inscricao_atividades.html',
                           participante=db.session.query(Participante).filter_by(
                               usuario=current_user).first(),
                           usuario=current_user, minicursos=minicursos, workshops=workshops, palestras=palestras)

@login_required
def inscricao_atividades_com_filtro(filtro):
    minicursos = db.session.query(Atividade).filter(
        Atividade.tipo.like(TipoAtividade['minicurso']), Atividade.titulo.like("%" + filtro + "%"))
    workshops = db.session.query(Atividade).filter(
        Atividade.tipo.like(TipoAtividade['workshop']), Atividade.titulo.like("%" + filtro + "%"))
    palestras = db.session.query(Atividade).filter(
        Atividade.tipo.like(TipoAtividade['palestra']), Atividade.titulo.like("%" + filtro + "%"))

    return render_template('inscricao_atividades.html',
                           participante=db.session.query(Participante).filter_by(
                               usuario=current_user).first(),
                           usuario=current_user, minicursos=minicursos, workshops=workshops, palestras=palestras)

@login_required
def inscrever(id):
    atv = db.session.query(Atividade).filter_by(id=id)[0]
    if atv.vagas_disponiveis > 0:
        atv.participantes.append(db.session.query(
            Participante).filter_by(usuario=current_user).first())
        atv.vagas_disponiveis = atv.vagas_disponiveis - 1
        db.session.flush()
        db.session.commit()
        minicursos = db.session.query(Atividade).filter_by(
            tipo=TipoAtividade['minicurso'])
        workshops = db.session.query(Atividade).filter_by(
            tipo=TipoAtividade['workshop'])
        palestras = db.session.query(Atividade).filter_by(
            tipo=TipoAtividade['palestra'])

        return render_template('inscricao_atividades.html',
                               participante=db.session.query(Participante).filter_by(
                                   usuario=current_user).first(),
                               usuario=current_user, minicursos=minicursos, workshops=workshops, palestras=palestras,
                               acao="+")
    else:
        return "Não há vagas disponíveis!"
    return id

@login_required
def desinscrever(id):
    atv = db.session.query(Atividade).filter_by(id=id).first()
    if db.session.query(Participante).filter_by(usuario=current_user).first() in atv.participantes:
        atv.participantes.remove(db.session.query(
            Participante).filter_by(usuario=current_user).first())
        atv.vagas_disponiveis = atv.vagas_disponiveis + 1
        db.session.flush()
        db.session.commit()
        minicursos = db.session.query(Atividade).filter_by(
            tipo=TipoAtividade['minicurso'])
        workshops = db.session.query(Atividade).filter_by(
            tipo=TipoAtividade['workshop'])
        palestras = db.session.query(Atividade).filter_by(
            tipo=TipoAtividade['palestra'])
        return render_template('inscricao_atividades.html',
                               participante=db.session.query(Participante).filter_by(
                                   usuario=current_user).first(),
                               usuario=current_user, minicursos=minicursos, workshops=workshops, palestras=palestras,
                               acao="-")
    else:
        return "Não está inscrito nessa atividade!"

@login_required
def alterar_senha():
    form = AlterarSenhaForm(request.form)
    if email_confirmado() == True:
        if form.validate_on_submit():
            usuario = db.session.query(Usuario).filter_by(
                email=current_user.email).first()
            enc = pbkdf2_sha256.encrypt(
                form.nova_senha.data, rounds=10000, salt_size=15)
            usuario.senha = enc
            db.session.add(usuario)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return render_template('alterar_senha.html', form=form, action=request.base_url)
    else:
        flash('Confirme seu e-mail para alterar a senha!')
        return redirect(url_for('dashboard_usuario'))

def esqueci_senha():
    form = AlterarSenhaPorEmailForm(request.form)
    if form.validate_on_submit():
        usuario = db.session.query(Usuario).filter_by(
            email=form.email.data).first()
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        salt = gensalt().decode('utf-8')
        token = serializer.dumps(usuario.email, salt=salt)
        usuario.salt_alteracao_senha = salt
        usuario.token_alteracao_senha = token
        db.session.add(usuario)
        db.session.commit()
        enviarEmailSenha(usuario, token)
        return render_template("esqueci_senha.html", status_envio_email=True, form=form)
    return render_template("esqueci_senha.html", status_envio_email=False, form=form)

def confirmar_alteracao_senha(token):
    form = AlterarSenhaForm(request.form)
    if form.validate_on_submit():
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            # Acha o usuário que possui o token
            usuario = db.session.query(Usuario).filter_by(
                token_alteracao_senha=token).first()
            salt = usuario.salt_alteracao_senha
            # Gera um email a partir do token do link e do salt do db
            email = serializer.loads(token, salt=salt, max_age=3600)
            hash = pbkdf2_sha256.encrypt(
            form.nova_senha.data, rounds=10000, salt_size=15)
            usuario.senha = hash
            _commit(usuario)
        except SignatureExpired:
            return "O link de confirmação expirou !"
        except Exception as e:
            print(e)
            return "Falha na confirmação de link do email"
        return redirect(url_for('login'))
    return render_template("alterar_senha.html", form=form, action=request.base_url)
