# Edx Xblock para la puntuación de vídeos#
Este XBlock permite puntuar vídeos y guardar dicha puntuación en una base de datos MySQL.

## Installation instructions ##
Para instalar el XBlock en tu Edx devstack Server necesitas lo siguiente:

## Descarga los archivos del xblock desde GitHub y copialos a tu servidor
##.   Instala tu xblock:
Debes reemplazar `/path/to/your/block` con la ruta a la que hayas descargado el xblock.

        $ vagrant ssh
        vagrant@precise64:~$ sudo -u edxapp /edx/bin/pip.edxapp install /path/to/your/block

##. Crear la tabla en el servidor MySQL
    
    #.  Conectate a tu servidor MySQL

    #.  Crea la tabla itemrating en tu servidor de MySQL

        #   mysql db_name < item_rating.sql

##. Configura la conexión a tu tabla en el XBlock.
    
    #.  Edita el fichero `/path/to/your/block/ratingvideo/settings.py`
    #.  Introduce los valores correctos para 'user','password','host','database'
    #.  Guarda los cambios

##.  Activa el XBlock

    #.  En ``edx-platform/lms/envs/common.py``, descomenta:

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  En ``edx-platform/cms/envs/common.py``, descomenta:

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  En ``edx-platform/cms/envs/common.py``, cambia:

            'ALLOW_ALL_ADVANCED_COMPONENTS': False,

        a:

            'ALLOW_ALL_ADVANCED_COMPONENTS': True,

##.  Añade el XBlock a tus opciones avanzadas de cursos en Studio.

    #. Abre sesión en Studio y dirígite al curso.
    #. Opciones -> Opciones avanzadas
    #. Cambia el valor de la llave ``"advanced_modules"`` a ``ratingvideo``


##.  Añade el bloque a tu curso

    #. Edita una unidad
    #. Avanzado -> tu-bloque

##. Deploying your XBlock

Para implementar su bloque a su propia versión hospedada de la plataforma edx, es necesario instalarlo en el virtualenv donde la plataforma se ejecuta, y añadirlo a la lista de``ADVANCED_COMPONENT_TYPES``
en ``edx-platform/cms/djangoapps/contentstore/views/component.py``.

#. Usando xblock en el curso

.En Studio ve a:

![Settings->Advanced Settings](https://appedx.uc3m.es/images/p7.jpg)

.Da de alta ratingvideo en la lista de modulos avanzados (advanced_modules)

![Settings->Advanced Settings](https://appedx.uc3m.es/images/p1.png)

.Después de esto, un nuevo botón llamado "Avanzado" aparecerá en tu vista de edición de las unidades.

![Advanced](https://appedx.uc3m.es/images/p8.jpg)

.Aparecerá una nueva opción llamada ratingVideo. Al pulsar añadirá el neuvo componente con el elemento para puntuar al curso.

![Advanced](https://appedx.uc3m.es/images/p2.png)

.Puedes cambiar los parametros del xblock ratingvideo pulsando el botón de editar. Puedes configurar si quieres mostrar el número de votos y la puntuación total.

![Edit](https://appedx.uc3m.es/images/p6.jpg)

.Ahora ya sólo queda cambiar el id del vídeo que hay que puntuar..

![Edit](https://appedx.uc3m.es/images/p9.jpg)