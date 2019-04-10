from app.models.models import *
from app.controllers.exceptions import *

def valida_participante(usuario):
    if Participante.participante_existe(usuario) == False:
        raise ParticipanteExiste
    elif email_confirmado() == False:
        raise EmailNaoConfirmado


def get_score_evento(edicao):
    return 10000


def get_participantes():
    try:
        query = db.session.query(Participante)
        participantes = []
        for p in query:
            info = (p.id, p.usuario.primeiro_nome + " " + p.usuario.sobrenome)
            participantes.append(info)
        return participantes
    except Exception as e:
        print(e)
        return None


def get_participantes_sem_kit():
    try:
        query = db.session.query(Participante).filter_by(pacote=0)
        participantes = []
        for p in query:
            info = (p.id, p.usuario.primeiro_nome + " " + p.usuario.sobrenome)
            participantes.append(info)
        return participantes
    except Exception as e:
        print(e)
        return None


def cadastra_objeto_generico(objeto):
    try:
        db.session.add(objeto)
        db.session.flush()
        db.session.commit()
        return objeto

    except Exception as e:
        print(e)
        return None
