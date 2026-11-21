from tclCommands.TclCommand import TclCommand

import collections

import gettext
import appTranslation as fcTranslate
import builtins

import appHandlers.appIO
import appObjects.GeometryObject
import importlib

fcTranslate.apply_language('strings')
if '_' not in builtins.__dict__:
    _ = gettext.gettext


class TclCommandExportAllDXF(TclCommand):
    """
    Tcl shell command to export a Geometry Object as an DXF File.

    example:
        export_all_dxf path/my_geometry ... filename
    """

    # List of all command aliases, to be able to use old names for backward compatibility (add_poly, add_polygon)
    aliases = ['export_all_dxf', 'eadxf']

    description = '%s %s' % ("--", "Export all Geometries object as a DXF File.")

    # Dictionary of types from Tcl command, needs to be ordered
    arg_names = collections.OrderedDict([
        ('filename', str)
    ])

    # Dictionary of types from Tcl command, needs to be ordered , this  is  for options  like -optionname value
    option_types = collections.OrderedDict([
    ])

    # array of mandatory options for current Tcl command: required = ['name','outname']
    required = ['filename']

    # structured help for current command, args needs to be ordered
    help = {
        'main': "Export Geometries object as a DXF File.",
        'args': collections.OrderedDict([
            ('filename', 'Absolute path to file to export.\n'
                         'WARNING: no spaces are allowed. If unsure enclose the entire path with quotes.'),
            ('name', 'Name of the Geometry object to export.'),
        ]),
        'examples': ['export_all_dxf path/my_file.dxf my_geo my_geo2', 'export_all_dxf D:/my_file.dxf my_geo my_geo2 ']
    }

    def execute(self, args, unnamed_args):
        """

        :param args:
        :param unnamed_args:
        :return:
        """
        if 'filename' not in args:
            return "Failed. The output filename was not provided."

        filename = args['filename']

        # if 'filename' not in args:
        #     filename = self.app.options["global_last_save_folder"] + '/' + args['name']
        # else:
        #     filename = args['filename']

        if len(unnamed_args) == 0:
            obj_names = None
            # self.raise_tcl_error("at least one name need")
        else:
            obj_names = unnamed_args
                # nr_points = int(len(unnamed_args) / 2)
        # source_obj_name = unnamed_args[0]

        importlib.reload(appHandlers.appIO)
        importlib.reload(appObjects.GeometryObject)

        self.app.f_handlers.export_all_dxf(obj_names=obj_names, filename=filename, use_thread=False)
