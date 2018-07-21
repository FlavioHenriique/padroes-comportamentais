from observer.observadores.Email import Email
from observer.observadores.Forum import Forum
from observer.observadores.Notification import Notification
from observer.observadores.SMS import SMS

forum = Forum()

forum.addObservador(SMS())
forum.addObservador(Email())
forum.addObservador(Notification())

forum.addTopico("Padrões")
forum.addTopico("POO")