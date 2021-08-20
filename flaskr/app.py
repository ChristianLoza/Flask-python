from flask_restful import Api

from flaskr import create_app
from .modelos import *
from .vistas import VistaCanciones, VistaCancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()


api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')


# with app.app_context():
    # album_schema = AlbumSchema()
    # usuario_schema = UsuarioSchema()
    # cancion_scehma = CancionSchema()
    # A = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    # db.session.add(A)
    # db.session.commit()

    ##REST
    # print([album_schema.dump(album) for album in Album.query.all()])
    # print([usuario_schema.dump(u) for u in Usuario.query.all()])
    # print([album_schema.dump(c) for c in Cancion.query.all()])

#test

# with app.app_context():
#     u = Usuario(nombre_usuario='Juan',contrasena='12345')
#     a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
#     c = Cancion(titulo= 'mi cancion', minutos=1, segundos=15,interprete='Juanito')
#     a.canciones.append(c)
#     u.albumes.append(a)
#     db.session.add(u)
#     db.session.add(c)
#     db.session.commit()
#     print(Usuario.query.all())
#     print(Usuario.query.all()[0].albumes)
#     db.session.delete(u)
#     print(Usuario.query.all())
#     print(Album.query.all()[0].canciones)
#     print(Cancion.query.all())

