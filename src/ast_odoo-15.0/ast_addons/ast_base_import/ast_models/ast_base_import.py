Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='binascii', asname=None)],
        ),
        Import(
            names=[alias(name='codecs', asname=None)],
        ),
        Import(
            names=[alias(name='collections', asname=None)],
        ),
        Import(
            names=[alias(name='difflib', asname=None)],
        ),
        Import(
            names=[alias(name='unicodedata', asname=None)],
        ),
        Import(
            names=[alias(name='chardet', asname=None)],
        ),
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        Import(
            names=[alias(name='operator', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        ImportFrom(
            module='PIL',
            names=[alias(name='Image', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.mimetypes',
            names=[alias(name='guess_mimetype', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='config', asname=None),
                alias(name='DEFAULT_SERVER_DATE_FORMAT', asname=None),
                alias(name='DEFAULT_SERVER_DATETIME_FORMAT', asname=None),
                alias(name='pycompat', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='FIELDS_RECURSION_LIMIT', ctx=Store())],
            value=Constant(value=3, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='ERROR_PREVIEW_BYTES', ctx=Store())],
            value=Constant(value=200, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_IMAGE_TIMEOUT', ctx=Store())],
            value=Constant(value=3, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_IMAGE_MAXBYTES', ctx=Store())],
            value=BinOp(
                left=BinOp(
                    left=Constant(value=10, kind=None),
                    op=Mult(),
                    right=Constant(value=1024, kind=None),
                ),
                op=Mult(),
                right=Constant(value=1024, kind=None),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_IMAGE_REGEX', ctx=Store())],
            value=Constant(value='^(?:http|https)://', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_IMAGE_CHUNK_SIZE', ctx=Store())],
            value=Constant(value=32768, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='IMAGE_FIELDS', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='icon', kind=None),
                    Constant(value='image', kind=None),
                    Constant(value='logo', kind=None),
                    Constant(value='picture', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='BOM_MAP', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='utf-16le', kind=None),
                    Constant(value='utf-16be', kind=None),
                    Constant(value='utf-32le', kind=None),
                    Constant(value='utf-32be', kind=None),
                ],
                values=[
                    Attribute(
                        value=Name(id='codecs', ctx=Load()),
                        attr='BOM_UTF16_LE',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='codecs', ctx=Load()),
                        attr='BOM_UTF16_BE',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='codecs', ctx=Load()),
                        attr='BOM_UTF32_LE',
                        ctx=Load(),
                    ),
                    Attribute(
                        value=Name(id='codecs', ctx=Load()),
                        attr='BOM_UTF32_BE',
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='xlrd', asname=None)],
                ),
                Try(
                    body=[
                        ImportFrom(
                            module='xlrd',
                            names=[alias(name='xlsx', asname=None)],
                            level=0,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='ImportError', ctx=Load()),
                            name=None,
                            body=[
                                Assign(
                                    targets=[Name(id='xlsx', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[
                                Name(id='xlrd', ctx=Store()),
                                Name(id='xlsx', ctx=Store()),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Try(
            body=[
                ImportFrom(
                    module=None,
                    names=[alias(name='odf_ods_reader', asname=None)],
                    level=1,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='odf_ods_reader', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Assign(
            targets=[Name(id='FILE_TYPE_DICT', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='text/csv', kind=None),
                    Constant(value='application/vnd.ms-excel', kind=None),
                    Constant(value='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', kind=None),
                    Constant(value='application/vnd.oasis.opendocument.spreadsheet', kind=None),
                ],
                values=[
                    Tuple(
                        elts=[
                            Constant(value='csv', kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=None, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='xls', kind=None),
                            Name(id='xlrd', ctx=Load()),
                            Constant(value='xlrd', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='xlsx', kind=None),
                            Name(id='xlsx', ctx=Load()),
                            Constant(value='xlrd >= 1.0.0', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ods', kind=None),
                            Name(id='odf_ods_reader', ctx=Load()),
                            Constant(value='odfpy', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='EXTENSIONS', ctx=Store())],
            value=DictComp(
                key=BinOp(
                    left=Constant(value='.', kind=None),
                    op=Add(),
                    right=Name(id='ext', ctx=Load()),
                ),
                value=Name(id='handler', ctx=Load()),
                generators=[
                    comprehension(
                        target=Tuple(
                            elts=[
                                Name(id='mime', ctx=Store()),
                                Tuple(
                                    elts=[
                                        Name(id='ext', ctx=Store()),
                                        Name(id='handler', ctx=Store()),
                                        Name(id='req', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            ctx=Store(),
                        ),
                        iter=Call(
                            func=Attribute(
                                value=Name(id='FILE_TYPE_DICT', ctx=Load()),
                                attr='items',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        ifs=[],
                        is_async=0,
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ImportValidationError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    This class is made to correctly format all the different error types that\n    can occur during the pre-validation of the import that is made before\n    calling the data loading itself. The Error data structure is meant to copy\n    the one of the errors raised during the data loading. It simplifies the\n    error management at client side as all errors can be treated the same way.\n\n    This exception is typically raised when there is an error during data\n    parsing (image, int, dates, etc..) or if the user did not select at least\n    one field to map with a column.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='message', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='error_type', kind=None),
                                    Constant(value='error', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='message',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='message', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='record',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='not_matching_error',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_path',
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='kwargs', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='field', kind=None)],
                                    keywords=[],
                                ),
                                body=List(
                                    elts=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='field', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='field_type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Base',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='base', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_import_templates',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Get the import templates label and path.\n\n        :return: a list(dict) containing label and template path\n                 like ``[{'label': 'foo', 'template': 'path'}]``\n        ", kind=None),
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ImportMapping',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" mapping of previous column:field selections\n\n    This is useful when repeatedly importing from a third-party\n    system: column names generated by the external system may\n    not match Odoo's field names or labels. This model is used\n    to save the mapping between column names and fields so that\n    next time a user imports from the same third-party systems\n    we can automatically match the columns to the correct field\n    without them having to re-enter the mapping every single\n    time.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='base_import.mapping', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Base Import Mapping', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_model', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='column_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='field_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ResUsers',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.users', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_can_import_remote_urls',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Hook to decide whether the current user is allowed to import\n        images via URL (as such an import can DOS a worker). By default,\n        allows the administrator group.\n\n        :rtype: bool\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_admin',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Import',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    This model is used to prepare the loading of data coming from a user file.\n\n    Here is the process that is followed:\n\n    #. The user selects a file to import.\n    #. File parsing and mapping suggestion (see "parse_preview" method)\n\n       #. Extract the current model\'s importable fields tree (see :meth:`get_fields_tree`).\n       #. Read the file (see :meth:`_read_file`) and extract header names and file\n          length (used for batch import).\n       #. Extract headers types from the data preview (10 first line of the file)\n          (see :meth:`_extract_headers_types`).\n       #. Try to find for each header a field to map with (see :meth:`_get_mapping_suggestions`)\n\n          - First check the previously saved mappings between the header name\n            and one of the model\'s fields.\n          - If no mapping found, try an exact match comparison using fields\n            technical names, labels and user language translated labels.\n          - If nothing found, try a fuzzy match using word distance between\n            header name and fields tachnical names, labels and user language\n            translated labels. Keep only the closest match.\n\n       #. Prepare examples for each columns using the first non null value from each column.\n       #. Send the info back to the UI where the user can modify the suggested mapping.\n    #. Execute the import: There are two import mode with uses the same process. (see :meth:`execute_import`)\n\n       #. Test import: Try to import but rollback the transaction. This allows\n          the check errors during the import process and allow the user to\n          choose import options for the different encountered errors.\n       #. Real import: Try to import the file using the configured mapping and\n          the eventual "error mapping options". If import encounters blocking\n          errors, the transaction is rollbacked and the user is allowed to\n          choose import options for the different errors.\n\n          - Get file data and fields to import into (see :meth:`_convert_import_data`).\n          - Parse date, float and binary data (see :meth:`_parse_import_data`).\n          - Handle multiple mapping -> concatenate char/text/many2many columns\n            mapped on the same field (see :meth:`_handle_multi_mapping`).\n          - Handle fallback values for boolean and selection fields, in case\n            input data does not match any allowed values (see :meth:`_handle_fallback_values`).\n          - Load data (see ir.model "load" method).\n          - Rollback transaction if test mode or if encountered error.\n          - Save mapping if any import is successful to ease later mapping suggestions.\n          - Return import result to the UI (success or errors if any).\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='base_import.import', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Base Import', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_transient_max_hours', ctx=Store())],
                    value=Constant(value=12.0, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='FUZZY_MATCH_DISTANCE', ctx=Store())],
                    value=Constant(value=0.2, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_model', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Model', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='file', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='File', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='File to check and/or import, raw binary (not base64)', kind=None),
                            ),
                            keyword(
                                arg='attachment',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='file_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='File Name', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='file_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='File Type', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_fields_tree',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='depth', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Name(id='FIELDS_RECURSION_LIMIT', ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Recursively get fields for the provided model (through\n        fields_get) and filter them according to importability\n\n        The output format is a list of :class:`Field`:\n\n        .. class:: Field\n\n            .. attribute:: id: str\n\n                A non-unique identifier for the field, used to compute\n                the span of the ``required`` attribute: if multiple\n                ``required`` fields have the same id, only one of them\n                is necessary.\n\n            .. attribute:: name: str\n\n                The field's logical (Odoo) name within the scope of\n                its parent.\n\n            .. attribute:: string: str\n\n                The field's human-readable name (``@string``)\n\n            .. attribute:: required: bool\n\n                Whether the field is marked as required in the\n                model. Clients must provide non-empty import values\n                for all required fields or the import will error out.\n\n            .. attribute:: fields: list[Field]\n\n                The current field's subfields. The database and\n                external identifiers for m2o and m2m fields; a\n                filtered and transformed fields_get for o2m fields (to\n                a variable depth defined by ``depth``).\n\n                Fields with no sub-fields will have an empty list of\n                sub-fields.\n\n            .. attribute:: model_name: str\n\n                Used in the Odoo Field Tooltip on the import view\n                and to get the model of the field of the related field(s).\n                Name of the current field's model.\n\n            .. attribute:: comodel_name: str\n\n                Used in the Odoo Field Tooltip on the import view\n                and to get the model of the field of the related field(s).\n                Name of the current field's comodel, i.e. if the field is a relation field.\n\n        Structure example for 'crm.team' model for returned importable_fields::\n\n            [\n                {'name': 'message_ids', 'string': 'Messages', 'model_name': 'crm.team', 'comodel_name': 'mail.message', 'fields': [\n                    {'name': 'moderation_status', 'string': 'Moderation Status', 'model_name': 'mail.message', 'fields': []},\n                    {'name': 'body', 'string': 'Contents', 'model_name': 'mail.message', 'fields' : []}\n                ]},\n                {{'name': 'name', 'string': 'Sales Team', 'model_name': 'crm.team', 'fields' : []}\n            ]\n\n        :param str model: name of the model to get fields form\n        :param int depth: depth of recursion into o2m fields\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Name(id='model', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='importable_fields', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='string', kind=None),
                                            Constant(value='required', kind=None),
                                            Constant(value='fields', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='id', kind=None),
                                            Constant(value='id', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='External ID', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='id', kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='depth', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='importable_fields', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='model_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Model', ctx=Load()),
                                    attr='fields_get',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='blacklist', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='models', ctx=Load()),
                                    attr='MAGIC_COLUMNS',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Attribute(
                                            value=Name(id='Model', ctx=Load()),
                                            attr='CONCURRENCY_CHECK_FIELD',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='name', ctx=Store()),
                                    Name(id='field', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='model_fields', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='name', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='blacklist', ctx=Load())],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='field', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='deprecated', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=False, kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='readonly', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='states', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='states', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='states', ctx=Load()),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='any', ctx=Load()),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='attr', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='readonly', kind=None)],
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='value', ctx=Load()),
                                                                        ops=[Is()],
                                                                        comparators=[Constant(value=False, kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Tuple(
                                                                        elts=[
                                                                            Name(id='attr', ctx=Store()),
                                                                            Name(id='value', ctx=Store()),
                                                                        ],
                                                                        ctx=Store(),
                                                                    ),
                                                                    iter=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='itertools', ctx=Load()),
                                                                                attr='chain',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='from_iterable',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='states', ctx=Load()),
                                                                                    attr='values',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='field_value', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='string', kind=None),
                                            Constant(value='required', kind=None),
                                            Constant(value='fields', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='model_name', kind=None),
                                        ],
                                        values=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                            Subscript(
                                                value=Name(id='field', ctx=Load()),
                                                slice=Constant(value='string', kind=None),
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='required', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Subscript(
                                                value=Name(id='field', ctx=Load()),
                                                slice=Constant(value='type', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='model', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='field', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='many2many', kind=None),
                                                    Constant(value='many2one', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='field_value', ctx=Load()),
                                                    slice=Constant(value='fields', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[Name(id='field_value', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='name',
                                                                value=Constant(value='id', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='string',
                                                                value=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='External ID', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='type',
                                                                value=Constant(value='id', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[Name(id='field_value', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='name',
                                                                value=Constant(value='.id', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='string',
                                                                value=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Database ID', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='type',
                                                                value=Constant(value='id', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='field_value', ctx=Load()),
                                                    slice=Constant(value='comodel_name', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='field', ctx=Load()),
                                                slice=Constant(value='relation', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='field', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='one2many', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='field_value', ctx=Load()),
                                                            slice=Constant(value='fields', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='get_fields_tree',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='field', ctx=Load()),
                                                                slice=Constant(value='relation', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='depth',
                                                                value=BinOp(
                                                                    left=Name(id='depth', ctx=Load()),
                                                                    op=Sub(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_has_groups',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='base.group_no_one', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='field_value', ctx=Load()),
                                                                        slice=Constant(value='fields', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='name', kind=None),
                                                                            Constant(value='string', kind=None),
                                                                            Constant(value='required', kind=None),
                                                                            Constant(value='fields', kind=None),
                                                                            Constant(value='type', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='.id', kind=None),
                                                                            Constant(value='.id', kind=None),
                                                                            Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='Database ID', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            List(elts=[], ctx=Load()),
                                                                            Constant(value='id', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='field_value', ctx=Load()),
                                                            slice=Constant(value='comodel_name', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='field', ctx=Load()),
                                                        slice=Constant(value='relation', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='importable_fields', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='field_value', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='importable_fields', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filter_fields_by_types',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model_fields_tree', annotation=None, type_comment=None),
                            arg(arg='header_types', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Remove from model_fields_tree param all the fields and subfields\n        that do not match the types in header_types\n\n        :param: list[dict] model_fields_tree: Contains recursively all the importable fields of the target model.\n                                              Generated in "get_fields_tree" method.\n        :param: list header_types: Contains the extracted fields types of the current header.\n                                   Generated in :meth:`_extract_header_types`.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='most_likely_fields_tree', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Name(id='model_fields_tree', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='subfields', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='fields', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='subfields', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='filtered_field', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='field', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='filtered_field', ctx=Load()),
                                                    slice=Constant(value='fields', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_filter_fields_by_types',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='subfields', ctx=Load()),
                                                    Name(id='header_types', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='most_likely_fields_tree', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='filtered_field', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='field', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='type', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='header_types', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='most_likely_fields_tree', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='field', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='most_likely_fields_tree', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_read_file',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Dispatch to specific method to read file content, according to its mimetype or file type\n\n        :param dict options: reading options (quoting, separator, ...)\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Name(id='guess_mimetype', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='file',
                                                ctx=Load(),
                                            ),
                                            Constant(value=b'', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='file_extension', ctx=Store()),
                                        Name(id='handler', ctx=Store()),
                                        Name(id='req', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='FILE_TYPE_DICT', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='handler', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='self', ctx=Load()),
                                                        BinOp(
                                                            left=Constant(value='_read_', kind=None),
                                                            op=Add(),
                                                            right=Name(id='file_extension', ctx=Load()),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                args=[Name(id='options', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value="Failed to read file '%s' (transient id %d) using guessed mimetype %s", kind=None),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='file_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='<unknown>', kind=None),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='mimetype', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='file_extension', ctx=Store()),
                                        Name(id='handler', ctx=Store()),
                                        Name(id='req', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='FILE_TYPE_DICT', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='file_type',
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='handler', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='self', ctx=Load()),
                                                        BinOp(
                                                            left=Constant(value='_read_', kind=None),
                                                            op=Add(),
                                                            right=Name(id='file_extension', ctx=Load()),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                args=[Name(id='options', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value="Failed to read file '%s' (transient id %d) using user-provided mimetype %s", kind=None),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='file_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='<unknown>', kind=None),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='file_type',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='file_name',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='p', ctx=Store()),
                                                Name(id='ext', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='splitext',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='file_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='ext', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='EXTENSIONS', ctx=Load())],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Call(
                                                            func=Name(id='getattr', ctx=Load()),
                                                            args=[
                                                                Name(id='self', ctx=Load()),
                                                                BinOp(
                                                                    left=Constant(value='_read_', kind=None),
                                                                    op=Add(),
                                                                    right=Subscript(
                                                                        value=Name(id='ext', ctx=Load()),
                                                                        slice=Slice(
                                                                            lower=Constant(value=1, kind=None),
                                                                            upper=None,
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        args=[Name(id='options', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value="Failed to read file '%s' (transient id %s) using file extension", kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='file_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='req', ctx=Load()),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ImportError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Unable to load "{extension}" file: requires Python module "{modname}"', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='extension',
                                                        value=Name(id='file_extension', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='modname',
                                                        value=Name(id='req', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Unsupported file format "{}", import only supports CSV, ODS, XLS and XLSX', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='file_type',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_read_xls',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='book', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xlrd', ctx=Load()),
                                    attr='open_workbook',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='file_contents',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='file',
                                                    ctx=Load(),
                                                ),
                                                Constant(value=b'', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='sheets', ctx=Store()),
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='sheets', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='book', ctx=Load()),
                                    attr='sheet_names',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='sheet', ctx=Store()),
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='sheet', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='sheet', kind=None)],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='sheets', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_read_xls_book',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='book', ctx=Load()),
                                    Name(id='sheet', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_read_xls_book',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='book', annotation=None, type_comment=None),
                            arg(arg='sheet_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='sheet', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='book', ctx=Load()),
                                    attr='sheet_by_name',
                                    ctx=Load(),
                                ),
                                args=[Name(id='sheet_name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rows', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='rowx', ctx=Store()),
                                    Name(id='row', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='map', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='sheet', ctx=Load()),
                                                attr='row',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='sheet', ctx=Load()),
                                                        attr='nrows',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='colx', ctx=Store()),
                                            Name(id='cell', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[
                                            Name(id='row', ctx=Load()),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='cell', ctx=Load()),
                                                    attr='ctype',
                                                    ctx=Load(),
                                                ),
                                                ops=[Is()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='xlrd', ctx=Load()),
                                                        attr='XL_CELL_NUMBER',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='is_float', ctx=Store())],
                                                    value=Compare(
                                                        left=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='cell', ctx=Load()),
                                                                attr='value',
                                                                ctx=Load(),
                                                            ),
                                                            op=Mod(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value=0.0, kind=None)],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            IfExp(
                                                                test=Name(id='is_float', ctx=Load()),
                                                                body=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='cell', ctx=Load()),
                                                                            attr='value',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                orelse=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Name(id='int', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='cell', ctx=Load()),
                                                                                    attr='value',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='cell', ctx=Load()),
                                                            attr='ctype',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Is()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='xlrd', ctx=Load()),
                                                                attr='XL_CELL_DATE',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='is_datetime', ctx=Store())],
                                                            value=Compare(
                                                                left=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='cell', ctx=Load()),
                                                                        attr='value',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Mod(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value=0.0, kind=None)],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='dt', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='datetime', ctx=Load()),
                                                                    attr='datetime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Starred(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='xlrd', ctx=Load()),
                                                                                    attr='xldate',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='xldate_as_tuple',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='cell', ctx=Load()),
                                                                                    attr='value',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Name(id='book', ctx=Load()),
                                                                                    attr='datemode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    IfExp(
                                                                        test=Name(id='is_datetime', ctx=Load()),
                                                                        body=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='dt', ctx=Load()),
                                                                                attr='strftime',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        orelse=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='dt', ctx=Load()),
                                                                                attr='strftime',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='DEFAULT_SERVER_DATE_FORMAT', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='cell', ctx=Load()),
                                                                    attr='ctype',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Is()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='xlrd', ctx=Load()),
                                                                        attr='XL_CELL_BOOLEAN',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            IfExp(
                                                                                test=Attribute(
                                                                                    value=Name(id='cell', ctx=Load()),
                                                                                    attr='value',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                body=Constant(value='True', kind='u'),
                                                                                orelse=Constant(value='False', kind='u'),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='cell', ctx=Load()),
                                                                            attr='ctype',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Is()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='xlrd', ctx=Load()),
                                                                                attr='XL_CELL_ERROR',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Raise(
                                                                            exc=Call(
                                                                                func=Name(id='ValueError', ctx=Load()),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Call(
                                                                                            func=Name(id='_', ctx=Load()),
                                                                                            args=[Constant(value='Invalid cell value at row %(row)s, column %(col)s: %(cell_value)s', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Mod(),
                                                                                        right=Dict(
                                                                                            keys=[
                                                                                                Constant(value='row', kind=None),
                                                                                                Constant(value='col', kind=None),
                                                                                                Constant(value='cell_value', kind=None),
                                                                                            ],
                                                                                            values=[
                                                                                                Name(id='rowx', ctx=Load()),
                                                                                                Name(id='colx', ctx=Load()),
                                                                                                Call(
                                                                                                    func=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='xlrd', ctx=Load()),
                                                                                                            attr='error_text_from_code',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='get',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[
                                                                                                        Attribute(
                                                                                                            value=Name(id='cell', ctx=Load()),
                                                                                                            attr='value',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        Call(
                                                                                                            func=Name(id='_', ctx=Load()),
                                                                                                            args=[
                                                                                                                Constant(value='unknown error code %s', kind=None),
                                                                                                                Attribute(
                                                                                                                    value=Name(id='cell', ctx=Load()),
                                                                                                                    attr='value',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                            ],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                    ],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            cause=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='values', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='cell', ctx=Load()),
                                                                                        attr='value',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='x', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Name(id='values', ctx=Load()),
                                                        ifs=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='strip',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='rows', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Name(id='sheet', ctx=Load()),
                                        attr='nrows',
                                        ctx=Load(),
                                    ),
                                    Name(id='rows', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_read_xlsx', ctx=Store())],
                    value=Name(id='_read_xls', ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_read_ods',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='doc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='odf_ods_reader', ctx=Load()),
                                    attr='ODSReader',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='file',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='io', ctx=Load()),
                                                attr='BytesIO',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='file',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=b'', kind=None),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='sheets', ctx=Store()),
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='sheets', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='doc', ctx=Load()),
                                                attr='SHEETS',
                                                ctx=Load(),
                                            ),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='sheet', ctx=Store()),
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='sheet', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='sheet', kind=None)],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='sheets', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='row', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='row', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='doc', ctx=Load()),
                                                attr='getSheet',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='sheet', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Name(id='x', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='x', ctx=Store()),
                                                                iter=Name(id='row', ctx=Load()),
                                                                ifs=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='x', ctx=Load()),
                                                                            attr='strip',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='content', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_read_csv',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns file length and a CSV-parsed list of all non-empty lines in the file.\n\n        :raises csv.Error: if an error is detected during CSV parsing\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='csv_data', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='file',
                                        ctx=Load(),
                                    ),
                                    Constant(value=b'', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='csv_data', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Tuple(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='encoding', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='encoding', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='encoding', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='encoding', ctx=Store()),
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='encoding', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='chardet', ctx=Load()),
                                                        attr='detect',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='csv_data', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value='encoding', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='bom', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='BOM_MAP', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='encoding', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='bom', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='csv_data', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='bom', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='encoding', ctx=Store()),
                                                Subscript(
                                                    value=Name(id='options', ctx=Load()),
                                                    slice=Constant(value='encoding', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='encoding', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='encoding', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='utf-8', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='csv_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='csv_data', ctx=Load()),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='encoding', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='separator', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='separator', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='separator', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='separator', ctx=Store())],
                                    value=Constant(value=',', kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='candidate', ctx=Store()),
                                    iter=Tuple(
                                        elts=[
                                            Constant(value=',', kind=None),
                                            Constant(value=';', kind=None),
                                            Constant(value='\t', kind=None),
                                            Constant(value=' ', kind=None),
                                            Constant(value='|', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='unicodedata', ctx=Load()),
                                                    attr='lookup',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='unit separator', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='it', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pycompat', ctx=Load()),
                                                    attr='csv_reader',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='io', ctx=Load()),
                                                            attr='BytesIO',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='csv_data', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='quotechar',
                                                        value=Subscript(
                                                            value=Name(id='options', ctx=Load()),
                                                            slice=Constant(value='quoting', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='delimiter',
                                                        value=Name(id='candidate', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='w', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='row', ctx=Store()),
                                            iter=Name(id='it', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='width', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='row', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='w', ctx=Load()),
                                                        ops=[Is()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='w', ctx=Store())],
                                                            value=Name(id='width', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='width', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='width', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[Name(id='w', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Name(id='separator', ctx=Store()),
                                                        Subscript(
                                                            value=Name(id='options', ctx=Load()),
                                                            slice=Constant(value='separator', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='candidate', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Break(),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='csv_iterator', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_reader',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='csv_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='quotechar',
                                        value=Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='quoting', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='delimiter',
                                        value=Name(id='separator', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='row', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='row', ctx=Store()),
                                        iter=Name(id='csv_iterator', ctx=Load()),
                                        ifs=[
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Name(id='x', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='x', ctx=Store()),
                                                                iter=Name(id='row', ctx=Load()),
                                                                ifs=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='x', ctx=Load()),
                                                                            attr='strip',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='content', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_extract_header_types',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='preview_values', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns the potential field types, based on the preview values, using heuristics.\n\n        This methods is only used for suggested mapping at 2 levels:\n\n        1. for fuzzy mapping at file load -> Execute the fuzzy mapping only\n           on "most likely field types"\n        2. For "Suggested fields" section in the fields mapping dropdown list at UI side.\n\n        The following heuristic is used: If all preview values\n\n        - Start with ``__export__``: return id + relational field types\n        - Can be cast into integer: return id + relational field types, integer, float and monetary\n        - Can be cast into Boolean: return boolean\n        - Can be cast into float: return float, monetary\n        - Can be cast into date/datetime: return date / datetime\n        - Cannot be cast into any of the previous types: return only text based fields\n\n        :param preview_values: list of value for the column to determine\n                               see :meth:`parse_preview` for more details.\n        :param options: parsing options\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[Name(id='preview_values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='values', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Set(
                                        elts=[Constant(value='', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[Constant(value='all', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='all', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='v', ctx=Load()),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='__export__', kind=None)],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='v', ctx=Store()),
                                                iter=Name(id='values', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='many2many', kind=None),
                                            Constant(value='many2one', kind=None),
                                            Constant(value='one2many', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='all', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='v', ctx=Load()),
                                                attr='isdigit',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='v', ctx=Store()),
                                                iter=Name(id='values', ctx=Load()),
                                                ifs=[Name(id='v', ctx=Load())],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='field_type', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='integer', kind=None),
                                            Constant(value='float', kind=None),
                                            Constant(value='monetary', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Set(
                                                elts=[
                                                    Constant(value='0', kind=None),
                                                    Constant(value='1', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            attr='issuperset',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='field_type', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='boolean', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='field_type', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='all', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Call(
                                                func=Attribute(
                                                    value=Name(id='val', ctx=Load()),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='true', kind=None),
                                                        Constant(value='false', kind=None),
                                                        Constant(value='t', kind=None),
                                                        Constant(value='f', kind=None),
                                                        Constant(value='', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='val', ctx=Store()),
                                                iter=Name(id='preview_values', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[Constant(value='boolean', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='thousand_separator', ctx=Store()),
                                        Name(id='decimal_separator', ctx=Store()),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='val', ctx=Store()),
                                    iter=Name(id='preview_values', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='val', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='val', ctx=Load()),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='val', ctx=Load()),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='val', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_remove_currency_symbol',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='val', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='val', ctx=Load()),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='options', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='float_thousand_separator', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='options', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='float_decimal_separator', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='val', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='val', ctx=Load()),
                                                                            attr='replace',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='options', ctx=Load()),
                                                                                slice=Constant(value='float_thousand_separator', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='options', ctx=Load()),
                                                                        slice=Constant(value='float_decimal_separator', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='.', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='val', ctx=Load()),
                                                                        attr='count',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='.', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='options', ctx=Load()),
                                                                            slice=Constant(value='float_thousand_separator', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='.', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='options', ctx=Load()),
                                                                            slice=Constant(value='float_decimal_separator', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value=',', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='val', ctx=Load()),
                                                                                attr='count',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value=',', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[Gt()],
                                                                        comparators=[Constant(value=1, kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='options', ctx=Load()),
                                                                                    slice=Constant(value='float_thousand_separator', kind=None),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value=',', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='options', ctx=Load()),
                                                                                    slice=Constant(value='float_decimal_separator', kind=None),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='.', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='val', ctx=Load()),
                                                                                        attr='find',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='.', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                ops=[Gt()],
                                                                                comparators=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='val', ctx=Load()),
                                                                                            attr='find',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value=',', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='thousand_separator', ctx=Store())],
                                                                                    value=Constant(value=',', kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='decimal_separator', ctx=Store())],
                                                                                    value=Constant(value='.', kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='val', ctx=Load()),
                                                                                                attr='find',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value=',', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        ops=[Gt()],
                                                                                        comparators=[
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='val', ctx=Load()),
                                                                                                    attr='find',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Constant(value='.', kind=None)],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='thousand_separator', ctx=Store())],
                                                                                            value=Constant(value='.', kind=None),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                        Assign(
                                                                                            targets=[Name(id='decimal_separator', ctx=Store())],
                                                                                            value=Constant(value=',', kind=None),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='float', ctx=Load()),
                                                        args=[Constant(value='a', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='thousand_separator', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='options', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='float_decimal_separator', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='options', ctx=Load()),
                                                    slice=Constant(value='float_thousand_separator', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='thousand_separator', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='options', ctx=Load()),
                                                    slice=Constant(value='float_decimal_separator', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='decimal_separator', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=List(
                                        elts=[
                                            Constant(value='float', kind=None),
                                            Constant(value='monetary', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_try_match_date_time',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='preview_values', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='results', ctx=Load()),
                            body=[
                                Return(
                                    value=Name(id='results', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='text', kind=None),
                                    Constant(value='char', kind=None),
                                    Constant(value='binary', kind=None),
                                    Constant(value='selection', kind=None),
                                    Constant(value='html', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_try_match_date_time',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='preview_values', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='date_patterns', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='date_format', kind=None)],
                                    keywords=[],
                                ),
                                body=List(
                                    elts=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='date_format', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                orelse=List(elts=[], ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_date_format', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.lang', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='_lang_get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='lang',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='date_format',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='user_date_format', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='to_re', ctx=Load()),
                                                args=[Name(id='user_date_format', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='date_patterns', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='user_date_format', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='KeyError', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='date_patterns', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[Name(id='DATE_PATTERNS', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Name(id='check_patterns', ctx=Load()),
                                args=[
                                    Name(id='date_patterns', ctx=Load()),
                                    Name(id='preview_values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='match', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='date_format', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='match', ctx=Load()),
                                    type_comment=None,
                                ),
                                Return(
                                    value=List(
                                        elts=[
                                            Constant(value='date', kind=None),
                                            Constant(value='datetime', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='datetime_patterns', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='datetime_format', kind=None)],
                                    keywords=[],
                                ),
                                body=List(
                                    elts=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='datetime_format', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                orelse=List(elts=[], ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime_patterns', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=BinOp(
                                            left=Constant(value='%s %s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Name(id='d', ctx=Load()),
                                                    Name(id='t', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='d', ctx=Store()),
                                                iter=Name(id='date_patterns', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                            comprehension(
                                                target=Name(id='t', ctx=Store()),
                                                iter=Name(id='TIME_PATTERNS', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Name(id='check_patterns', ctx=Load()),
                                args=[
                                    Name(id='datetime_patterns', ctx=Load()),
                                    Name(id='preview_values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='match', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='datetime_format', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='match', ctx=Load()),
                                    type_comment=None,
                                ),
                                Return(
                                    value=List(
                                        elts=[Constant(value='datetime', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_extract_headers_types',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='headers', annotation=None, type_comment=None),
                            arg(arg='preview', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        For each column, this method will extract the potential data types based on the preview values\n\n        :param list headers: list of headers names. Used as part of key for\n                             returned headers_types to ease understanding of its usage\n        :param list preview: list of the first file records (see "parse_preview" for more detail) e.g.::\n\n            [ ["lead_name1", "1", "partner_id1"], ["lead_name2", "2", "partner_id2"], ... ]\n\n        :param options: parsing options\n        :returns: dict headers_types:\n\n            contains all the extracted header types for each header e.g.::\n\n                {\n                    (header_index, header_name): ["char", "text", ...],\n                    ...\n                }\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='headers_types', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='column_index', ctx=Store()),
                                    Name(id='header_name', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='headers', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='preview_values', ctx=Store())],
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='record', ctx=Load()),
                                                    slice=Name(id='column_index', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='record', ctx=Store()),
                                                iter=Name(id='preview', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='type_field', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_extract_header_types',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='preview_values', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='headers_types', ctx=Load()),
                                            slice=Tuple(
                                                elts=[
                                                    Name(id='column_index', ctx=Load()),
                                                    Name(id='header_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='type_field', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='headers_types', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_mapping_suggestion',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='header', annotation=None, type_comment=None),
                            arg(arg='fields_tree', annotation=None, type_comment=None),
                            arg(arg='header_types', annotation=None, type_comment=None),
                            arg(arg='mapping_fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Attempts to match a given header to a field of the imported model.\n\n            We can distinguish 2 types of header format:\n\n            - simple header string that aim to directly match a field of the target model\n              e.g.: "lead_id" or "Opportunities" or "description".\n            - composed \'/\' joined header string that aim to match a field of a\n              relation field of the target model (= subfield) e.g.:\n              \'lead_id/description\' aim to match the field ``description`` of the field lead_id.\n\n            When returning result, to ease further treatments, the result is\n            returned as a list, where each element of the list is a field or\n            a sub-field of the preceding field.\n\n            - ``["lead_id"]`` for simple case = simple matching\n            - ``["lead_id", "description"]`` for composed case = hierarchy matching\n\n            Mapping suggestion is found using the following heuristic:\n\n            - first we check if there was a saved mapping by the user\n            - then try to make an exact match on the field technical name /\n              english label / translated label\n            - finally, try the "fuzzy match": word distance between the header\n              title and the field technical name / english label / translated\n              label, using the lowest result. The field used for the fuzzy match\n              are based on the field types we extracted from the header data\n              (see :meth:`_extract_header_types`).\n\n            For subfields, use the same logic.\n\n            Word distance is a score between 0 and 1 to express the distance\n            between two char strings where ``0`` denotes an exact match and\n            ``1`` indicates completely different strings\n\n            In order to keep only one column matched per field, we return the\n            distance. That distance will be used during the deduplicate process\n            (see :meth:`_deduplicate_mapping_suggestions`) and only the\n            mapping with the smallest distance will be kept in case of multiple\n            mapping on the same field. Note that we don\'t need to return the\n            distance in case of hierachy mapping as we consider that as an\n            advanced behaviour. The deduplicate process will ignore hierarchy\n            mapping. The user will have to manually select on which field he\n            wants to map what in case of mapping duplicates for sub-fields.\n\n            :param str header: header name from the file\n            :param list fields_tree: list of all the field of the target model\n                Coming from :meth:`get_fields_tree`\n                e.g: ``[ { \'name\': \'fieldName\', \'string\': \'fieldLabel\', fields: [ { \'name\': \'subfieldName\', ...} ]} , ... ]``\n            :param list header_types: Extracted field types for each column in the parsed file, based on its data content.\n                Coming from :meth:`_extract_header_types`\n                e.g.: ``[\'int\', \'float\', \'char\', \'many2one\', ...]``\n            :param dict mapping_fields: contains the previously saved mapping between header and field for the current model.\n                E.g.: ``{ header_name: field_name }``\n            :returns: if the header couldn\'t be matched: an empty dict\n                      else: a dict with the field path and the distance between header and the matched field.\n            :rtype: ``dict(field_path + Word distance)``\n\n                    In case of simple matching: ``{\'field_path\': [field_name], distance: word_distance}``\n                                           e.g.: ``{\'field_path\': [\'lead_id\'], distance: 0.23254}``\n                    In case of hierarchy matching: ``{\'field_path\': [parent_field_name, child_field_name, subchild_field_name]}``\n                                              e.g.: ``{\'field_path\': [\'lead_id\', \'description\']}``\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='fields_tree', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mapping_field_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mapping_fields', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='header', ctx=Load()),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='mapping_field_name', ctx=Load()),
                                    Name(id='mapping_field_name', ctx=Load()),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='field_path', kind=None),
                                            Constant(value='distance', kind=None),
                                        ],
                                        values=[
                                            ListComp(
                                                elt=Name(id='name', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='name', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='mapping_field_name', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='/', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='/', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='header', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='IrTranslation', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='translated_header', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='IrTranslation', ctx=Load()),
                                                    attr='_get_source',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='ir.model.fields,field_description', kind=None),
                                                    Constant(value='model', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='lang',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='header', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=Name(id='fields_tree', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='header', ctx=Load()),
                                                        attr='casefold',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='field', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='casefold',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='field_string', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='string', kind=None),
                                                            Constant(value='', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='casefold',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='translated_header', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='field_string', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='header', ctx=Load()),
                                                                attr='casefold',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='field_string', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='field', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='field', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[
                                                    Constant(value='field_path', kind=None),
                                                    Constant(value='distance', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Subscript(
                                                                value=Name(id='field', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='filtered_fields', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_filter_fields_by_types',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fields_tree', ctx=Load()),
                                            Name(id='header_types', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='filtered_fields', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(keys=[], values=[]),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='min_dist', ctx=Store())],
                                    value=Constant(value=1, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='min_dist_field', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=Name(id='filtered_fields', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='field_string', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='string', kind=None),
                                                            Constant(value='', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='casefold',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='name_field_dist', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_distance',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='header', ctx=Load()),
                                                            attr='casefold',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='field', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='casefold',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='string_field_dist', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_distance',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='header', ctx=Load()),
                                                            attr='casefold',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Name(id='field_string', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='translated_string_field_dist', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_distance',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='translated_header', ctx=Load()),
                                                            attr='casefold',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Name(id='field_string', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='current_field_dist', ctx=Store())],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='name_field_dist', ctx=Load()),
                                                            Name(id='string_field_dist', ctx=Load()),
                                                            Name(id='translated_string_field_dist', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='current_field_dist', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Name(id='min_dist', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='min_dist_field', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='field', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='min_dist', ctx=Store())],
                                                    value=Name(id='current_field_dist', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='min_dist', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='FUZZY_MATCH_DISTANCE',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[
                                                    Constant(value='field_path', kind=None),
                                                    Constant(value='distance', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[Name(id='min_dist_field', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='min_dist', ctx=Load()),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='field_path', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subfields_tree', ctx=Store())],
                            value=Name(id='fields_tree', ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='sub_header', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='header', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_mapping_suggestion',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='sub_header', ctx=Load()),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='subfields_tree', ctx=Load()),
                                            Name(id='header_types', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='match', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(keys=[], values=[]),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='field_name', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='match', ctx=Load()),
                                            slice=Constant(value='field_path', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='subfields_tree', ctx=Store())],
                                    value=Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Subscript(
                                                    value=Name(id='item', ctx=Load()),
                                                    slice=Constant(value='fields', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='item', ctx=Store()),
                                                        iter=Name(id='subfields_tree', ctx=Load()),
                                                        ifs=[
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='item', ctx=Load()),
                                                                    slice=Constant(value='name', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='field_name', ctx=Load())],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field_path', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='field_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='field_path', kind=None)],
                                values=[Name(id='field_path', ctx=Load())],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_distance',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='a', annotation=None, type_comment=None),
                            arg(arg='b', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This method return an index that reflects the distance between the\n        two given string a and b.\n\n        This index is a score between 0 and 1 where ``0`` indicates an exact\n        match and ``1`` indicates completely different strings.\n        ', kind=None),
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value=1, kind=None),
                                op=Sub(),
                                right=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='difflib', ctx=Load()),
                                                attr='SequenceMatcher',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value=None, kind=None),
                                                Name(id='a', ctx=Load()),
                                                Name(id='b', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='ratio',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_mapping_suggestions',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='headers', annotation=None, type_comment=None),
                            arg(arg='header_types', annotation=None, type_comment=None),
                            arg(arg='fields_tree', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Attempts to match the imported model's fields to the\n            titles of the parsed CSV file, if the file is supposed to have\n            headers.\n\n            Returns a dict mapping cell indices to key paths in the ``fields`` tree.\n\n            :param list headers: titles of the parsed file\n            :param dict header_types:\n\n                extracted types for each column in the parsed file e.g.::\n\n                    {\n                        (header_index, header_name): ['int', 'float', 'char', 'many2one',...],\n                         ...\n                    }\n\n            :param list fields_tree:\n\n                list of the target model's fields e.g.::\n\n                    [\n                        {\n                            'name': 'fieldName',\n                            'string': 'fieldLabel',\n                            'fields': [{ 'name': 'subfieldName', ...}]\n                        },\n                        ...\n                    ]\n\n            :rtype: dict[(int, str), {'field_path': list[str], 'distance': int}]\n            :returns: mapping_suggestions e.g.:\n\n                .. code-block:: python\n\n                    {\n                        (header_index, header_name): {\n                            'field_path': ['child_id','name'],\n                            'distance': 0\n                        },\n                        ...\n                    }\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mapping_suggestions', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapping_records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.mapping', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='res_model',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='column_name', kind=None),
                                            Constant(value='field_name', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapping_fields', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='rec', ctx=Load()),
                                    slice=Constant(value='column_name', kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='rec', ctx=Load()),
                                    slice=Constant(value='field_name', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='rec', ctx=Store()),
                                        iter=Name(id='mapping_records', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='index', ctx=Store()),
                                    Name(id='header', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='headers', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='match_field', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_mapping_suggestion',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='header', ctx=Load()),
                                            Name(id='fields_tree', ctx=Load()),
                                            Subscript(
                                                value=Name(id='header_types', ctx=Load()),
                                                slice=Tuple(
                                                    elts=[
                                                        Name(id='index', ctx=Load()),
                                                        Name(id='header', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            Name(id='mapping_fields', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='mapping_suggestions', ctx=Load()),
                                            slice=Tuple(
                                                elts=[
                                                    Name(id='index', ctx=Load()),
                                                    Name(id='header', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='match_field', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_deduplicate_mapping_suggestions',
                                    ctx=Load(),
                                ),
                                args=[Name(id='mapping_suggestions', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='mapping_suggestions', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_deduplicate_mapping_suggestions',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mapping_suggestions', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" This method is meant to avoid multiple columns to be matched on the same field.\n\n        Taking ``mapping_suggestions`` as input, it will check if multiple\n        columns are mapped to the same field and will only keep the mapping\n        that has the smallest distance. The other columns that were matched\n        to the same field are removed from the mapping suggestions.\n\n        Hierarchy mapping is considered as advanced and is skipped during this\n        deduplication process. We consider that multiple mapping on hierarchy\n        mapping will not occur often and due to the fact that this won't lead\n        to any particular issues when a non 'char/text' field is selected more\n        than once in the UI, we keep only the last selected mapping. The\n        objective is to lighten the mapping suggestion process as much as we can.\n\n        :param dict mapping_suggestions: ``{ (column_index, header_name) : { 'field_path': [header_name], 'distance': word_distance }}``\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='min_dist_per_field', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers_to_keep', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='header', ctx=Store()),
                                    Name(id='suggestion', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='mapping_suggestions', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Name(id='suggestion', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='suggestion', ctx=Load()),
                                                            slice=Constant(value='field_path', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='headers_to_keep', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='header', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='field_name', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='suggestion', ctx=Load()),
                                            slice=Constant(value='field_path', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='field_distance', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='suggestion', ctx=Load()),
                                        slice=Constant(value='distance', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='best_distance', ctx=Store()),
                                                Name(id='_best_header', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='min_dist_per_field', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field_name', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='field_distance', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Name(id='best_distance', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='min_dist_per_field', ctx=Load()),
                                                    slice=Name(id='field_name', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='field_distance', ctx=Load()),
                                                    Name(id='header', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers_to_keep', ctx=Store())],
                            value=BinOp(
                                left=Name(id='headers_to_keep', ctx=Load()),
                                op=Add(),
                                right=ListComp(
                                    elt=Subscript(
                                        value=Name(id='value', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='value', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='min_dist_per_field', ctx=Load()),
                                                    attr='values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='header', ctx=Store()),
                            iter=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='mapping_suggestions', ctx=Load()),
                                        attr='keys',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Name(id='headers_to_keep', ctx=Load()),
                            ),
                            body=[
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='mapping_suggestions', ctx=Load()),
                                            slice=Name(id='header', ctx=Load()),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='parse_preview',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='count', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=10, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Generates a preview of the uploaded files, and performs\n            fields-matching between the import's file data and the model's\n            columns.\n\n            If the headers are not requested (not options.has_headers),\n            returned ``matches`` and ``headers`` are both ``False``.\n\n            :param int count: number of preview lines to generate\n            :param options: format-specific options.\n                            CSV: {quoting, separator, headers}\n            :type options: {str, str, str, bool}\n            :returns: ``{fields, matches, headers, preview} | {error, preview}``\n            :rtype: {dict(str: dict(...)), dict(int, list(str)), list(str), list(list(str))} | {str, str}\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='fields_tree', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_fields_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_model',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='file_length', ctx=Store()),
                                                Name(id='rows', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_read_file',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='options', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='file_length', ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ImportValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Import file has no content or is corrupt', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='preview', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='rows', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Name(id='count', ctx=Load()),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='has_headers', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='preview', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='headers', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='preview', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='header_types', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_extract_headers_types',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='headers', ctx=Load()),
                                                    Name(id='preview', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='header_types', ctx=Store()),
                                                        Name(id='headers', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Dict(keys=[], values=[]),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='matches', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='keep_matches', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='fields', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='index', ctx=Store()),
                                                    Name(id='match', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Name(id='enumerate', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='options', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='fields', kind=None),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='match', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='matches', ctx=Load()),
                                                                    slice=Name(id='index', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='match', ctx=Load()),
                                                                    attr='split',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='/', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='has_headers', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='matches', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_mapping_suggestions',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='headers', ctx=Load()),
                                                            Name(id='header_types', ctx=Load()),
                                                            Name(id='fields_tree', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='matches', ctx=Store())],
                                                    value=DictComp(
                                                        key=Subscript(
                                                            value=Name(id='header_key', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        value=Subscript(
                                                            value=Name(id='suggestion', ctx=Load()),
                                                            slice=Constant(value='field_path', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Tuple(
                                                                    elts=[
                                                                        Name(id='header_key', ctx=Store()),
                                                                        Name(id='suggestion', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='matches', ctx=Load()),
                                                                        attr='items',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[Name(id='suggestion', ctx=Load())],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='keep_matches', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='advanced_mode', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='advanced', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='has_relational_header', ctx=Store())],
                                            value=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='models', ctx=Load()),
                                                                            attr='fix_import_export_id_paths',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='col', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            ops=[Gt()],
                                                            comparators=[Constant(value=1, kind=None)],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='col', ctx=Store()),
                                                                iter=Name(id='headers', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='has_relational_match', ctx=Store())],
                                            value=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[Name(id='match', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            ops=[Gt()],
                                                            comparators=[Constant(value=1, kind=None)],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Tuple(
                                                                    elts=[
                                                                        Name(id='field', ctx=Store()),
                                                                        Name(id='match', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='matches', ctx=Load()),
                                                                        attr='items',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[Name(id='match', ctx=Load())],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='advanced_mode', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='has_relational_header', ctx=Load()),
                                                    Name(id='has_relational_match', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='column_example', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='column_index', ctx=Store()),
                                            Name(id='_unused', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='preview', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='vals', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='record', ctx=Store()),
                                            iter=Name(id='preview', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=Name(id='column_index', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='vals', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='%s%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Subscript(
                                                                                    value=Subscript(
                                                                                        value=Name(id='record', ctx=Load()),
                                                                                        slice=Name(id='column_index', ctx=Load()),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Slice(
                                                                                        lower=None,
                                                                                        upper=Constant(value=50, kind=None),
                                                                                        step=None,
                                                                                    ),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                IfExp(
                                                                                    test=Compare(
                                                                                        left=Call(
                                                                                            func=Name(id='len', ctx=Load()),
                                                                                            args=[
                                                                                                Subscript(
                                                                                                    value=Name(id='record', ctx=Load()),
                                                                                                    slice=Name(id='column_index', ctx=Load()),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        ops=[Gt()],
                                                                                        comparators=[Constant(value=50, kind=None)],
                                                                                    ),
                                                                                    body=Constant(value='...', kind=None),
                                                                                    orelse=Constant(value='', kind=None),
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='vals', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=5, kind=None)],
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='column_example', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='vals', ctx=Load()),
                                                            List(
                                                                elts=[Constant(value='', kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='batch', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='batch_cutoff', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='limit', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='batch_cutoff', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='count', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Name(id='batch_cutoff', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='batch', ctx=Store())],
                                                    value=Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='preview', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Name(id='batch_cutoff', ctx=Load())],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='batch', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='bool', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='next', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='itertools', ctx=Load()),
                                                                            attr='islice',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='rows', ctx=Load()),
                                                                            BinOp(
                                                                                left=Name(id='batch_cutoff', ctx=Load()),
                                                                                op=Sub(),
                                                                                right=Name(id='count', ctx=Load()),
                                                                            ),
                                                                            Constant(value=None, kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value=None, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='fields', kind=None),
                                            Constant(value='matches', kind=None),
                                            Constant(value='headers', kind=None),
                                            Constant(value='header_types', kind=None),
                                            Constant(value='preview', kind=None),
                                            Constant(value='options', kind=None),
                                            Constant(value='advanced_mode', kind=None),
                                            Constant(value='debug', kind=None),
                                            Constant(value='batch', kind=None),
                                            Constant(value='file_length', kind=None),
                                        ],
                                        values=[
                                            Name(id='fields_tree', ctx=Load()),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='matches', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='headers', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='header_types', ctx=Load()),
                                                                    attr='values',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Name(id='column_example', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Name(id='advanced_mode', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_has_groups',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='base.group_no_one', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='batch', ctx=Load()),
                                            Name(id='file_length', ctx=Load()),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='error',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Error during parsing preview', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='exc_info',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='preview', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='file_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='text/csv', kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='file',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='preview', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='file',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Name(id='ERROR_PREVIEW_BYTES', ctx=Load()),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='iso-8859-1', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Dict(
                                                keys=[
                                                    Constant(value='error', kind=None),
                                                    Constant(value='preview', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='error', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Name(id='preview', ctx=Load()),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_convert_import_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Extracts the input BaseModel and fields list (with\n            ``False``-y placeholders for fields to *not* import) into a\n            format Model.import_data can use: a fields list without holes\n            and the precisely matching data matrix\n\n            :param list(str|bool): fields\n            :returns: (data, fields)\n            :rtype: (list(list(str)), list(str))\n            :raises ValueError: in case the import data could not be converted\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='indices', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='index', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='index', ctx=Store()),
                                                Name(id='field', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Name(id='enumerate', ctx=Load()),
                                            args=[Name(id='fields', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='field', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='indices', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ImportValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You must configure at least one field to import', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='indices', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mapper', ctx=Store())],
                                    value=Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='row', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=List(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Subscript(
                                                        value=Name(id='indices', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='mapper', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='operator', ctx=Load()),
                                            attr='itemgetter',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='indices', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='import_fields', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='f', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='f', ctx=Store()),
                                        iter=Name(id='fields', ctx=Load()),
                                        ifs=[Name(id='f', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='_file_length', ctx=Store()),
                                        Name(id='rows_to_import', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_read_file',
                                    ctx=Load(),
                                ),
                                args=[Name(id='options', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='has_headers', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rows_to_import', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='rows_to_import', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[Name(id='row', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='row', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='map', ctx=Load()),
                                            args=[
                                                Name(id='mapper', ctx=Load()),
                                                Name(id='rows_to_import', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[Name(id='row', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Slice(
                                            lower=Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='skip', kind=None)],
                                                keywords=[],
                                            ),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(id='import_fields', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_remove_currency_symbol',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='value', ctx=Load()),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='negative', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='value', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='(', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='value', ctx=Load()),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=')', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='value', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='negative', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='float_regex', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='compile',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='([+-]?[0-9.,]+)', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='split_value', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='g', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='g', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='float_regex', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='value', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='g', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='split_value', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=2, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='split_value', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='float_regex', ctx=Load()),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='split_value', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=IfExp(
                                                test=UnaryOp(
                                                    op=Not(),
                                                    operand=Name(id='negative', ctx=Load()),
                                                ),
                                                body=Subscript(
                                                    value=Name(id='split_value', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=BinOp(
                                                    left=Constant(value='-', kind=None),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Name(id='split_value', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='currency_index', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='float_regex', ctx=Load()),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='split_value', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='currency_index', ctx=Store())],
                                            value=Constant(value=1, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='currency', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.currency', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='symbol', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='split_value', ctx=Load()),
                                                                        slice=Name(id='currency_index', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strip',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='currency', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Return(
                                            value=IfExp(
                                                test=UnaryOp(
                                                    op=Not(),
                                                    operand=Name(id='negative', ctx=Load()),
                                                ),
                                                body=Subscript(
                                                    value=Name(id='split_value', ctx=Load()),
                                                    slice=BinOp(
                                                        left=BinOp(
                                                            left=Name(id='currency_index', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                        op=Mod(),
                                                        right=Constant(value=2, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                orelse=BinOp(
                                                    left=Constant(value='-', kind=None),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Name(id='split_value', ctx=Load()),
                                                        slice=BinOp(
                                                            left=BinOp(
                                                                left=Name(id='currency_index', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            op=Mod(),
                                                            right=Constant(value=2, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_float_from_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='index', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='line', ctx=Load()),
                                            slice=Name(id='index', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Name(id='index', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='line', ctx=Load()),
                                            slice=Name(id='index', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='thousand_separator', ctx=Store()),
                                                Name(id='decimal_separator', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_infer_separators',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Name(id='index', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Constant(value='E', kind=None),
                                                ops=[In()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Name(id='index', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Constant(value='e', kind=None),
                                                ops=[In()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Name(id='index', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='tmp_value', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Name(id='index', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='thousand_separator', ctx=Load()),
                                                    Constant(value='.', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='tmp_value', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value='{:f}', kind=None),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='float', ctx=Load()),
                                                                args=[Name(id='tmp_value', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='line', ctx=Load()),
                                                            slice=Name(id='index', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='tmp_value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='thousand_separator', ctx=Store())],
                                                    value=Constant(value=' ', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name=None,
                                                    body=[Pass()],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='line', ctx=Load()),
                                            slice=Name(id='index', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Name(id='index', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='thousand_separator', ctx=Load()),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='decimal_separator', ctx=Load()),
                                            Constant(value='.', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='old_value', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='line', ctx=Load()),
                                        slice=Name(id='index', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='line', ctx=Load()),
                                            slice=Name(id='index', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_remove_currency_symbol',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Name(id='index', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='line', ctx=Load()),
                                            slice=Name(id='index', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        ops=[Is()],
                                        comparators=[Constant(value=False, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ImportValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Column %s contains incorrect values (value: %s)', kind=None),
                                                            Name(id='name', ctx=Load()),
                                                            Name(id='old_value', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='field',
                                                        value=Name(id='name', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_infer_separators',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Try to infer the shape of the separators: if there are two\n        different "non-numberic" characters in the number, the\n        former/duplicated one would be grouping ("thousands" separator) and\n        the latter would be the decimal separator. The decimal separator\n        should furthermore be unique.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='non_number', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='c', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='c', ctx=Store()),
                                        iter=Name(id='value', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Name(id='c', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Constant(value='()-+', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='unicodedata', ctx=Load()),
                                                        attr='category',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='c', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='Nd', kind=None),
                                                            Constant(value='Sc', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='counts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='collections', ctx=Load()),
                                    attr='Counter',
                                    ctx=Load(),
                                ),
                                args=[Name(id='non_number', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='counts', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='counts', ctx=Load()),
                                            slice=Subscript(
                                                value=Name(id='non_number', ctx=Load()),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=ListComp(
                                        elt=Name(id='character', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='character', ctx=Store()),
                                                        Name(id='_count', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='counts', ctx=Load()),
                                                        attr='most_common',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='thousand_separator', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='float_thousand_separator', kind=None),
                                    Constant(value=' ', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='decimal_separator', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='float_decimal_separator', kind=None),
                                    Constant(value='.', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='thousand_separator', ctx=Load()),
                                    Name(id='decimal_separator', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_import_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='import_fields', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Lauch first call to :meth:`_parse_import_data_recursive` with an\n        empty prefix. :meth:`_parse_import_data_recursive` will be run\n        recursively for each relational field.\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_parse_import_data_recursive',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_model',
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                    Name(id='data', ctx=Load()),
                                    Name(id='import_fields', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_import_data_recursive',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='prefix', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='import_fields', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='all_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='fields_get',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='name', ctx=Store()),
                                    Name(id='field', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='all_fields', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='prefix', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='name', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='field', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='datetime', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='import_fields', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='index', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='import_fields', ctx=Load()),
                                                    attr='index',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_parse_date_from_data',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='data', ctx=Load()),
                                                    Name(id='index', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='field', ctx=Load()),
                                                        slice=Constant(value='type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Compare(
                                                                    left=BinOp(
                                                                        left=Name(id='name', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value='/', kind=None),
                                                                    ),
                                                                    ops=[In()],
                                                                    comparators=[Name(id='import_field', ctx=Load())],
                                                                ),
                                                                Compare(
                                                                    left=Name(id='name', ctx=Load()),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Subscript(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='import_field', ctx=Load()),
                                                                                    attr='split',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='/', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            slice=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='prefix', ctx=Load()),
                                                                                    attr='count',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='/', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='import_field', ctx=Store()),
                                                                iter=Name(id='import_fields', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_parse_import_data_recursive',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='field', ctx=Load()),
                                                                slice=Constant(value='relation', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=Name(id='name', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value='/', kind=None),
                                                            ),
                                                            Name(id='data', ctx=Load()),
                                                            Name(id='import_fields', ctx=Load()),
                                                            Name(id='options', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='field', ctx=Load()),
                                                                    slice=Constant(value='type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='float', kind=None),
                                                                            Constant(value='monetary', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Name(id='name', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[Name(id='import_fields', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='index', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='import_fields', ctx=Load()),
                                                                    attr='index',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_parse_float_from_data',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='data', ctx=Load()),
                                                                    Name(id='index', ctx=Load()),
                                                                    Name(id='name', ctx=Load()),
                                                                    Name(id='options', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='field', ctx=Load()),
                                                                            slice=Constant(value='type', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='binary', kind=None)],
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='field', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='attachment', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='any', ctx=Load()),
                                                                        args=[
                                                                            GeneratorExp(
                                                                                elt=Compare(
                                                                                    left=Name(id='f', ctx=Load()),
                                                                                    ops=[In()],
                                                                                    comparators=[Name(id='name', ctx=Load())],
                                                                                ),
                                                                                generators=[
                                                                                    comprehension(
                                                                                        target=Name(id='f', ctx=Store()),
                                                                                        iter=Name(id='IMAGE_FIELDS', ctx=Load()),
                                                                                        ifs=[],
                                                                                        is_async=0,
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='name', ctx=Load()),
                                                                        ops=[In()],
                                                                        comparators=[Name(id='import_fields', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='index', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='import_fields', ctx=Load()),
                                                                            attr='index',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='name', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                With(
                                                                    items=[
                                                                        withitem(
                                                                            context_expr=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='requests', ctx=Load()),
                                                                                    attr='Session',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            optional_vars=Name(id='session', ctx=Store()),
                                                                        ),
                                                                    ],
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='session', ctx=Load()),
                                                                                    attr='stream',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value=True, kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                        For(
                                                                            target=Tuple(
                                                                                elts=[
                                                                                    Name(id='num', ctx=Store()),
                                                                                    Name(id='line', ctx=Store()),
                                                                                ],
                                                                                ctx=Store(),
                                                                            ),
                                                                            iter=Call(
                                                                                func=Name(id='enumerate', ctx=Load()),
                                                                                args=[Name(id='data', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            body=[
                                                                                If(
                                                                                    test=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='re', ctx=Load()),
                                                                                            attr='match',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='config', ctx=Load()),
                                                                                                    attr='get',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    Constant(value='import_image_regex', kind=None),
                                                                                                    Name(id='DEFAULT_IMAGE_REGEX', ctx=Load()),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            Subscript(
                                                                                                value=Name(id='line', ctx=Load()),
                                                                                                slice=Name(id='index', ctx=Load()),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    body=[
                                                                                        If(
                                                                                            test=UnaryOp(
                                                                                                op=Not(),
                                                                                                operand=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='env',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='user',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='_can_import_remote_urls',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                            ),
                                                                                            body=[
                                                                                                Raise(
                                                                                                    exc=Call(
                                                                                                        func=Name(id='ImportValidationError', ctx=Load()),
                                                                                                        args=[
                                                                                                            Call(
                                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                                args=[Constant(value='You can not import images via URL, check with your administrator or support for the reason.', kind=None)],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ],
                                                                                                        keywords=[
                                                                                                            keyword(
                                                                                                                arg='field',
                                                                                                                value=Name(id='name', ctx=Load()),
                                                                                                            ),
                                                                                                            keyword(
                                                                                                                arg='field_type',
                                                                                                                value=Subscript(
                                                                                                                    value=Name(id='field', ctx=Load()),
                                                                                                                    slice=Constant(value='type', kind=None),
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    cause=None,
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[],
                                                                                        ),
                                                                                        Assign(
                                                                                            targets=[
                                                                                                Subscript(
                                                                                                    value=Name(id='line', ctx=Load()),
                                                                                                    slice=Name(id='index', ctx=Load()),
                                                                                                    ctx=Store(),
                                                                                                ),
                                                                                            ],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='_import_image_by_url',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    Subscript(
                                                                                                        value=Name(id='line', ctx=Load()),
                                                                                                        slice=Name(id='index', ctx=Load()),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Name(id='session', ctx=Load()),
                                                                                                    Name(id='name', ctx=Load()),
                                                                                                    Name(id='num', ctx=Load()),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        Try(
                                                                                            body=[
                                                                                                Expr(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='base64', ctx=Load()),
                                                                                                            attr='b64decode',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            Subscript(
                                                                                                                value=Name(id='line', ctx=Load()),
                                                                                                                slice=Name(id='index', ctx=Load()),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                        keywords=[
                                                                                                            keyword(
                                                                                                                arg='validate',
                                                                                                                value=Constant(value=True, kind=None),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            handlers=[
                                                                                                ExceptHandler(
                                                                                                    type=Attribute(
                                                                                                        value=Name(id='binascii', ctx=Load()),
                                                                                                        attr='Error',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    name=None,
                                                                                                    body=[
                                                                                                        Raise(
                                                                                                            exc=Call(
                                                                                                                func=Name(id='ImportValidationError', ctx=Load()),
                                                                                                                args=[
                                                                                                                    Call(
                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                        args=[Constant(value='Found invalid image data, images should be imported as either URLs or base64-encoded data.', kind=None)],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                keywords=[
                                                                                                                    keyword(
                                                                                                                        arg='field',
                                                                                                                        value=Name(id='name', ctx=Load()),
                                                                                                                    ),
                                                                                                                    keyword(
                                                                                                                        arg='field_type',
                                                                                                                        value=Subscript(
                                                                                                                            value=Name(id='field', ctx=Load()),
                                                                                                                            slice=Constant(value='type', kind=None),
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                ],
                                                                                                            ),
                                                                                                            cause=None,
                                                                                                        ),
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[],
                                                                                            finalbody=[],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_parse_date_from_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='index', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='field_type', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Attribute(
                                value=Name(id='datetime', ctx=Load()),
                                attr='datetime',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fmt', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='field_type', ctx=Load()),
                                    ops=[Eq()],
                                    comparators=[Constant(value='date', kind=None)],
                                ),
                                body=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='d_fmt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='date_format', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dt_fmt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='datetime_format', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='num', ctx=Store()),
                                    Name(id='line', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='line', ctx=Load()),
                                            slice=Name(id='index', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='v', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Name(id='index', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='dt_fmt', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='field_type', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='datetime', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    slice=Name(id='index', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Name(id='fmt', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='dt', ctx=Load()),
                                                                            attr='strptime',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='v', ctx=Load()),
                                                                            Name(id='dt_fmt', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Continue(),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='ValueError', ctx=Load()),
                                                            name=None,
                                                            body=[Pass()],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=Name(id='index', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='fmt', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='dt', ctx=Load()),
                                                            attr='strptime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='v', ctx=Load()),
                                                            Name(id='d_fmt', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ImportValidationError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Column %s contains incorrect values. Error in line %d: %s', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='name', ctx=Load()),
                                                                        BinOp(
                                                                            left=Name(id='num', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value=1, kind=None),
                                                                        ),
                                                                        Name(id='e', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='field',
                                                                value=Name(id='name', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='field_type',
                                                                value=Name(id='field_type', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ImportValidationError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Error Parsing Date [%s:L%d]: %s', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='name', ctx=Load()),
                                                                        BinOp(
                                                                            left=Name(id='num', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value=1, kind=None),
                                                                        ),
                                                                        Name(id='e', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='field',
                                                                value=Name(id='name', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='field_type',
                                                                value=Name(id='field_type', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_import_image_by_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='session', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='line_number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Imports an image by URL\n\n        :param str url: the original field value\n        :param requests.Session session:\n        :param str field: name of the field (for logging/debugging)\n        :param int line_number: 0-indexed line number within the imported file (for logging/debugging)\n        :return: the replacement value\n        :rtype: bytes\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='maxsize', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='config', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='import_image_maxbytes', kind=None),
                                            Name(id='DEFAULT_IMAGE_MAXBYTES', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='Trying to import image from URL: %s into field %s, at line %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='url', ctx=Load()),
                                                Name(id='field', ctx=Load()),
                                                Name(id='line_number', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='session', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='url', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='timeout',
                                                value=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='config', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='import_image_timeout', kind=None),
                                                                Name(id='DEFAULT_IMAGE_TIMEOUT', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='raise_for_status',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='response', ctx=Load()),
                                                        attr='headers',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Content-Length', kind=None)],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='response', ctx=Load()),
                                                                attr='headers',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='Content-Length', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Name(id='maxsize', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ImportValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='File size exceeds configured maximum (%s bytes)', kind=None),
                                                            Name(id='maxsize', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='field',
                                                        value=Name(id='field', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=Call(
                                        func=Name(id='bytearray', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='chunk', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='iter_content',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='DEFAULT_IMAGE_CHUNK_SIZE', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='content', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='chunk', ctx=Load()),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='content', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Name(id='maxsize', ctx=Load())],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ImportValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='File size exceeds configured maximum (%s bytes)', kind=None),
                                                                    Name(id='maxsize', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='field',
                                                                value=Name(id='field', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='open',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='io', ctx=Load()),
                                                    attr='BytesIO',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='content', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='w', ctx=Store()),
                                                Name(id='h', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='image', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='w', ctx=Load()),
                                            op=Mult(),
                                            right=Name(id='h', ctx=Load()),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=42000000.0, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ImportValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Image size excessive, imported images must be smaller than 42 million pixel', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='field',
                                                        value=Name(id='field', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ImportValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Could not retrieve URL: %(url)s [%(field_name)s: L%(line_number)d]: %(error)s', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='url',
                                                                value=Name(id='url', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='field_name',
                                                                value=Name(id='field', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='line_number',
                                                                value=BinOp(
                                                                    left=Name(id='line_number', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='error',
                                                                value=Name(id='e', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='field',
                                                        value=Name(id='field', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='execute_import',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='columns', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='dryrun', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Actual execution of the import\n\n        :param fields: import mapping: maps each column to a field,\n                       ``False`` for the columns to ignore\n        :type fields: list(str|bool)\n        :param columns: columns label\n        :type columns: list(str|bool)\n        :param dict options:\n        :param bool dryrun: performs all import operations (and\n                            validations) but rollbacks writes, allows\n                            getting as much errors as possible without\n                            the risk of clobbering the database.\n        :returns: A list of errors. If the list is empty the import\n                  executed fully and correctly. If the list is\n                  non-empty it contains dicts with 3 keys:\n\n                  ``type``\n                    the type of error (``error|warning``)\n                  ``message``\n                    the error message associated with the error (a string)\n                  ``record``\n                    the data which failed to import (or ``false`` if that data\n                    isn't available or provided)\n        :rtype: dict(ids: list(int), messages: list({type, message, record}))\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='SAVEPOINT import', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='input_file_data', ctx=Store()),
                                                Name(id='import_fields', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_convert_import_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fields', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='input_file_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_parse_import_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='input_file_data', ctx=Load()),
                                            Name(id='import_fields', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ImportValidationError', ctx=Load()),
                                    name='error',
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='messages', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='error', ctx=Load()),
                                                                attr='__dict__',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='importing %d rows...', kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='input_file_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='import_fields', ctx=Store()),
                                        Name(id='merged_data', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_handle_multi_mapping',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='import_fields', ctx=Load()),
                                    Name(id='input_file_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fallback_values', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='merged_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_handle_fallback_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='import_fields', ctx=Load()),
                                            Name(id='merged_data', ctx=Load()),
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='fallback_values', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='name_create_enabled_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='name_create_enabled_fields', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_limit', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='limit', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='res_model',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='import_file',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='name_create_enabled_fields',
                                        value=Name(id='name_create_enabled_fields', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='import_set_empty_fields',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='options', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='import_set_empty_fields', kind=None),
                                                List(elts=[], ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='import_skip_records',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='options', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='import_skip_records', kind=None),
                                                List(elts=[], ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='_import_limit',
                                        value=Name(id='import_limit', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model', ctx=Load()),
                                    attr='load',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='import_fields', ctx=Load()),
                                    Name(id='merged_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='done', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                If(
                                    test=Name(id='dryrun', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ROLLBACK TO SAVEPOINT import', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='pool',
                                                        ctx=Load(),
                                                    ),
                                                    attr='clear_caches',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='pool',
                                                        ctx=Load(),
                                                    ),
                                                    attr='reset_changes',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='RELEASE SAVEPOINT import', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='psycopg2', ctx=Load()),
                                        attr='InternalError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Subscript(
                                        value=Name(id='import_result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='has_headers', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='BaseImportMapping', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='base_import.mapping', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='index', ctx=Store()),
                                            Name(id='column_name', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='columns', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Name(id='column_name', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='mapping_domain', ctx=Store())],
                                                    value=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='res_model', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='res_model',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='column_name', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='column_name', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='column_mapping', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='BaseImportMapping', ctx=Load()),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='mapping_domain', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='limit',
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='column_mapping', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='column_mapping', ctx=Load()),
                                                                    attr='field_name',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[
                                                                    Subscript(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        slice=Name(id='index', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='column_mapping', ctx=Load()),
                                                                            attr='field_name',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Subscript(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        slice=Name(id='index', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='BaseImportMapping', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='res_model', kind=None),
                                                                            Constant(value='column_name', kind=None),
                                                                            Constant(value='field_name', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='res_model',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='column_name', ctx=Load()),
                                                                            Subscript(
                                                                                value=Name(id='fields', ctx=Load()),
                                                                                slice=Name(id='index', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='name', kind=None),
                                ops=[In()],
                                comparators=[Name(id='import_fields', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='index_of_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='import_fields', ctx=Load()),
                                            attr='index',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='skipped', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='skip', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Name(id='r', ctx=Store()),
                                        Subscript(
                                            value=Name(id='import_result', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=List(
                                            elts=[Constant(value='', kind=None)],
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Name(id='skipped', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Subscript(
                                                    value=Name(id='x', ctx=Load()),
                                                    slice=Name(id='index_of_name', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Subscript(
                                                            value=Name(id='input_file_data', ctx=Load()),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=Name(id='import_limit', ctx=Load()),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=List(
                                                    elts=[Constant(value='', kind=None)],
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=BinOp(
                                                    left=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='input_file_data', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    op=Sub(),
                                                    right=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='import_limit', ctx=Load()),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='import_result', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='skip', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='skip', kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='import_result', ctx=Load()),
                                slice=Constant(value='nextrow', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='import_result', ctx=Load()),
                                        slice=Constant(value='nextrow', kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Name(id='skip', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='import_result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_multi_mapping',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='import_fields', annotation=None, type_comment=None),
                            arg(arg='input_file_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' This method handles multiple mapping on the same field.\n\n        It will return the list of the mapped fields and the concatenated data for each field:\n\n        - If two column are mapped on the same text or char field, they will end up\n          in only one column, concatenated via space (char) or new line (text).\n        - The same logic is used for many2many fields. Multiple values can be\n          imported if they are separated by ``,``.\n\n        Input/output Example:\n\n        input data\n            .. code-block:: python\n\n                [\n                    ["Value part 1", "1", "res.partner_id1", "Value part 2"],\n                    ["I am", "1", "res.partner_id1", "Batman"],\n                ]\n\n        import_fields\n            ``[desc, some_number, partner, desc]``\n\n        output merged_data\n            .. code-block:: python\n\n                [\n                    ["Value part 1 Value part 2", "1", "res.partner_id1"],\n                    ["I am Batman", "1", "res.partner_id1"],\n                ]\n        fields\n            ``[desc, some_number, partner]``\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mapped_field_indexes', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='idx', ctx=Store()),
                                    Name(id='field', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='field', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field', ctx=Store()),
                                                iter=Name(id='import_fields', ctx=Load()),
                                                ifs=[Name(id='field', ctx=Load())],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='mapped_field_indexes', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='field', ctx=Load()),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='idx', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='import_fields', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='mapped_field_indexes', ctx=Load()),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='merged_data', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='input_file_data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='new_record', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='fields', ctx=Store()),
                                            Name(id='indexes', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='mapped_field_indexes', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='split_fields', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='target_field', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='split_fields', ctx=Load()),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='target_model', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_model',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='field', ctx=Store()),
                                            iter=Name(id='split_fields', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='field', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='target_field', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='target_model', ctx=Store())],
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Name(id='target_model', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(id='field', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_name',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='field_type', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Name(id='target_model', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='fields_get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='target_field', ctx=Load()),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='field_type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='char', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='new_record', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Constant(value=' ', kind=None),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Subscript(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            slice=Name(id='idx', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='idx', ctx=Store()),
                                                                                iter=Name(id='indexes', ctx=Load()),
                                                                                ifs=[
                                                                                    Subscript(
                                                                                        value=Name(id='record', ctx=Load()),
                                                                                        slice=Name(id='idx', ctx=Load()),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='field_type', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='text', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='new_record', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Constant(value='\n', kind=None),
                                                                            attr='join',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            GeneratorExp(
                                                                                elt=Subscript(
                                                                                    value=Name(id='record', ctx=Load()),
                                                                                    slice=Name(id='idx', ctx=Load()),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                generators=[
                                                                                    comprehension(
                                                                                        target=Name(id='idx', ctx=Store()),
                                                                                        iter=Name(id='indexes', ctx=Load()),
                                                                                        ifs=[
                                                                                            Subscript(
                                                                                                value=Name(id='record', ctx=Load()),
                                                                                                slice=Name(id='idx', ctx=Load()),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        is_async=0,
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='field_type', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='many2many', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='new_record', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Constant(value=',', kind=None),
                                                                                    attr='join',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    GeneratorExp(
                                                                                        elt=Subscript(
                                                                                            value=Name(id='record', ctx=Load()),
                                                                                            slice=Name(id='idx', ctx=Load()),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        generators=[
                                                                                            comprehension(
                                                                                                target=Name(id='idx', ctx=Store()),
                                                                                                iter=Name(id='indexes', ctx=Load()),
                                                                                                ifs=[
                                                                                                    Subscript(
                                                                                                        value=Name(id='record', ctx=Load()),
                                                                                                        slice=Name(id='idx', ctx=Load()),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                                is_async=0,
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='new_record', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='record', ctx=Load()),
                                                                                slice=Subscript(
                                                                                    value=Name(id='indexes', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='merged_data', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='new_record', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='import_fields', ctx=Load()),
                                    Name(id='merged_data', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_fallback_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='import_field', annotation=None, type_comment=None),
                            arg(arg='input_file_data', annotation=None, type_comment=None),
                            arg(arg='fallback_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        If there are fallback values, this method will replace the input file\n        data value if it does not match the possible values for the given field.\n        This is only valid for boolean and selection fields.\n\n        .. note::\n\n            We can consider that we need to retrieve the selection values for\n            all the fields in fallback_values, as if they are present, it's because\n            there was already a conflict during first import run and user had to\n            select a fallback value for the field.\n\n        :param: list import_field: ordered list of field that have been matched to import data\n        :param: list input_file_data: ordered list of values (list) that need to be imported in the given import_fields\n        :param: dict fallback_values:\n\n            contains all the fields that have been tagged by the user to use a\n            specific fallback value in case the value to import does not match\n            values accepted by the field (selection or boolean) e.g.::\n\n                {\n                    'fieldName': {\n                        'fallback_value': fallback_value,\n                        'field_model': field_model,\n                        'field_type': field_type\n                    },\n                    'state': {\n                        'fallback_value': 'draft',\n                        'field_model': field_model,\n                        'field_type': 'selection'\n                    },\n                    'active': {\n                        'fallback_value': 'true',\n                        'field_model': field_model,\n                        'field_type': 'boolean'\n                    }\n                }\n        ", kind=None),
                        ),
                        For(
                            target=Name(id='field_string', ctx=Store()),
                            iter=Name(id='fallback_values', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Subscript(
                                                value=Name(id='fallback_values', ctx=Load()),
                                                slice=Name(id='field_string', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='field_type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='selection', kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='field_path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field_string', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='target_field', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='field_path', ctx=Load()),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='target_model', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Subscript(
                                            value=Subscript(
                                                value=Name(id='fallback_values', ctx=Load()),
                                                slice=Name(id='field_string', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='field_model', kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='selection_values', ctx=Store())],
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='value', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='key', ctx=Store()),
                                                        Name(id='value', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Subscript(
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='target_model', ctx=Load()),
                                                                attr='fields_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Name(id='target_field', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        slice=Name(id='target_field', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='selection', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='fallback_values', ctx=Load()),
                                                slice=Name(id='field_string', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='selection_values', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='selection_values', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='record_index', ctx=Store()),
                                    Name(id='records', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='input_file_data', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='column_index', ctx=Store()),
                                            Name(id='value', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='records', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='field', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='import_field', ctx=Load()),
                                                slice=Name(id='column_index', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='field', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='fallback_values', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='fallback_value', ctx=Store())],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='fallback_values', ctx=Load()),
                                                            slice=Name(id='field', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='fallback_value', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='fallback_values', ctx=Load()),
                                                                slice=Name(id='field', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='field_type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='boolean', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='value', ctx=Store())],
                                                            value=IfExp(
                                                                test=Compare(
                                                                    left=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='value', ctx=Load()),
                                                                            attr='lower',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    ops=[In()],
                                                                    comparators=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='0', kind=None),
                                                                                Constant(value='1', kind=None),
                                                                                Constant(value='true', kind=None),
                                                                                Constant(value='false', kind=None),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                body=Name(id='value', ctx=Load()),
                                                                orelse=Name(id='fallback_value', ctx=Load()),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='value', ctx=Load()),
                                                                        attr='lower',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='fallback_values', ctx=Load()),
                                                                            slice=Name(id='field', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='selection_values', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='value', ctx=Store())],
                                                                    value=IfExp(
                                                                        test=Compare(
                                                                            left=Name(id='fallback_value', ctx=Load()),
                                                                            ops=[NotEq()],
                                                                            comparators=[Constant(value='skip', kind=None)],
                                                                        ),
                                                                        body=Name(id='fallback_value', ctx=Load()),
                                                                        orelse=Constant(value=None, kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='input_file_data', ctx=Load()),
                                                                slice=Name(id='record_index', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='column_index', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='input_file_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='_SEPARATORS', ctx=Store())],
            value=List(
                elts=[
                    Constant(value=' ', kind=None),
                    Constant(value='/', kind=None),
                    Constant(value='-', kind=None),
                    Constant(value='', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_PATTERN_BASELINE', ctx=Store())],
            value=List(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='%m', kind=None),
                            Constant(value='%d', kind=None),
                            Constant(value='%Y', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='%d', kind=None),
                            Constant(value='%m', kind=None),
                            Constant(value='%Y', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='%Y', kind=None),
                            Constant(value='%m', kind=None),
                            Constant(value='%d', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='%Y', kind=None),
                            Constant(value='%d', kind=None),
                            Constant(value='%m', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DATE_FORMATS', ctx=Store())],
            value=List(elts=[], ctx=Load()),
            type_comment=None,
        ),
        For(
            target=Name(id='ps', ctx=Store()),
            iter=Name(id='_PATTERN_BASELINE', ctx=Load()),
            body=[
                Assign(
                    targets=[Name(id='patterns', ctx=Store())],
                    value=Set(
                        elts=[Name(id='ps', ctx=Load())],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='s', ctx=Store()),
                            Name(id='t', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='%Y', kind=None),
                                    Constant(value='%y', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='patterns', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=IfExp(
                                                        test=Compare(
                                                            left=Name(id='it', ctx=Load()),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='s', ctx=Load())],
                                                        ),
                                                        body=Name(id='t', ctx=Load()),
                                                        orelse=Name(id='it', ctx=Load()),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='it', ctx=Store()),
                                                            iter=Name(id='f', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='f', ctx=Store()),
                                                iter=Name(id='patterns', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='DATE_FORMATS', ctx=Load()),
                            attr='extend',
                            ctx=Load(),
                        ),
                        args=[Name(id='patterns', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            orelse=[],
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DATE_PATTERNS', ctx=Store())],
            value=ListComp(
                elt=Call(
                    func=Attribute(
                        value=Name(id='sep', ctx=Load()),
                        attr='join',
                        ctx=Load(),
                    ),
                    args=[Name(id='fmt', ctx=Load())],
                    keywords=[],
                ),
                generators=[
                    comprehension(
                        target=Name(id='sep', ctx=Store()),
                        iter=Name(id='_SEPARATORS', ctx=Load()),
                        ifs=[],
                        is_async=0,
                    ),
                    comprehension(
                        target=Name(id='fmt', ctx=Store()),
                        iter=Name(id='DATE_FORMATS', ctx=Load()),
                        ifs=[],
                        is_async=0,
                    ),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TIME_PATTERNS', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='%H:%M:%S', kind=None),
                    Constant(value='%H:%M', kind=None),
                    Constant(value='%H', kind=None),
                    Constant(value='%I:%M:%S %p', kind=None),
                    Constant(value='%I:%M %p', kind=None),
                    Constant(value='%I %p', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='check_patterns',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='patterns', annotation=None, type_comment=None),
                    arg(arg='values', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                For(
                    target=Name(id='pattern', ctx=Store()),
                    iter=Name(id='patterns', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='p', ctx=Store())],
                            value=Call(
                                func=Name(id='to_re', ctx=Load()),
                                args=[Name(id='pattern', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='val', ctx=Store()),
                            iter=Name(id='values', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='val', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='match',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='val', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Name(id='pattern', ctx=Load()),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Constant(value=None, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='to_re',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='pattern', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' cut down version of TimeRE converting strptime patterns to regex\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='pattern', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='\\s+', kind=None),
                            Constant(value='\\\\s+', kind=None),
                            Name(id='pattern', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pattern', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='%([a-z])', kind=None),
                            Name(id='_replacer', ctx=Load()),
                            Name(id='pattern', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='flags',
                                value=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='IGNORECASE',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pattern', ctx=Store())],
                    value=BinOp(
                        left=BinOp(
                            left=Constant(value='^', kind=None),
                            op=Add(),
                            right=Name(id='pattern', ctx=Load()),
                        ),
                        op=Add(),
                        right=Constant(value='$', kind=None),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='pattern', ctx=Load()),
                            Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='IGNORECASE',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_replacer',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='m', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Subscript(
                        value=Name(id='_P_TO_RE', ctx=Load()),
                        slice=Call(
                            func=Attribute(
                                value=Name(id='m', ctx=Load()),
                                attr='group',
                                ctx=Load(),
                            ),
                            args=[Constant(value=1, kind=None)],
                            keywords=[],
                        ),
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_P_TO_RE', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='d', kind=None),
                    Constant(value='H', kind=None),
                    Constant(value='I', kind=None),
                    Constant(value='m', kind=None),
                    Constant(value='M', kind=None),
                    Constant(value='S', kind=None),
                    Constant(value='y', kind=None),
                    Constant(value='Y', kind=None),
                    Constant(value='p', kind=None),
                    Constant(value='%', kind=None),
                ],
                values=[
                    Constant(value='(3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])', kind=None),
                    Constant(value='(2[0-3]|[0-1]\\d|\\d)', kind=None),
                    Constant(value='(1[0-2]|0[1-9]|[1-9])', kind=None),
                    Constant(value='(1[0-2]|0[1-9]|[1-9])', kind=None),
                    Constant(value='([0-5]\\d|\\d)', kind=None),
                    Constant(value='(6[0-1]|[0-5]\\d|\\d)', kind=None),
                    Constant(value='(\\d\\d)', kind=None),
                    Constant(value='(\\d\\d\\d\\d)', kind=None),
                    Constant(value='(am|pm)', kind=None),
                    Constant(value='%', kind=None),
                ],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
