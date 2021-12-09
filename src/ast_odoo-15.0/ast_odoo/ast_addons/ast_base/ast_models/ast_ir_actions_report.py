Module(
    body=[
        ImportFrom(
            module='markupsafe',
            names=[alias(name='Markup', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='AccessError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.safe_eval',
            names=[
                alias(name='safe_eval', asname=None),
                alias(name='time', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='find_in_path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='config', asname=None),
                alias(name='is_html_empty', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.sql_db',
            names=[alias(name='TestCursor', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[
                alias(name='NEGATIVE_TERM_OPERATORS', asname=None),
                alias(name='FALSE_DOMAIN', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='lxml.html', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='contextlib',
            names=[alias(name='closing', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='distutils.version',
            names=[alias(name='LooseVersion', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='reportlab.graphics.barcode',
            names=[alias(name='createBarcodeDrawing', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='PyPDF2',
            names=[
                alias(name='PdfFileWriter', asname=None),
                alias(name='PdfFileReader', asname=None),
                alias(name='utils', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='collections.abc',
            names=[alias(name='Iterable', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='PIL',
            names=[
                alias(name='Image', asname=None),
                alias(name='ImageFile', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='ImageFile', ctx=Load()),
                    attr='LOAD_TRUNCATED_IMAGES',
                    ctx=Store(),
                ),
            ],
            value=Constant(value=True, kind=None),
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
        Try(
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='createBarcodeDrawing', ctx=Load()),
                                args=[Constant(value='Code128', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='value',
                                        value=Constant(value='foo', kind=None),
                                    ),
                                    keyword(
                                        arg='format',
                                        value=Constant(value='png', kind=None),
                                    ),
                                    keyword(
                                        arg='width',
                                        value=Constant(value=100, kind=None),
                                    ),
                                    keyword(
                                        arg='height',
                                        value=Constant(value=100, kind=None),
                                    ),
                                    keyword(
                                        arg='humanReadable',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            attr='asString',
                            ctx=Load(),
                        ),
                        args=[Constant(value='png', kind=None)],
                        keywords=[],
                    ),
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
        FunctionDef(
            name='_get_wkhtmltopdf_bin',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Return(
                    value=Call(
                        func=Name(id='find_in_path', ctx=Load()),
                        args=[Constant(value='wkhtmltopdf', kind=None)],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='wkhtmltopdf_state', ctx=Store())],
            value=Constant(value='install', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='wkhtmltopdf_dpi_zoom_ratio', ctx=Store())],
            value=Constant(value=False, kind=None),
            type_comment=None,
        ),
        Try(
            body=[
                Assign(
                    targets=[Name(id='process', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='Popen',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Call(
                                        func=Name(id='_get_wkhtmltopdf_bin', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='--version', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='stdout',
                                value=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='PIPE',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='stderr',
                                value=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='PIPE',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Tuple(
                        elts=[
                            Name(id='OSError', ctx=Load()),
                            Name(id='IOError', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                    name=None,
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='You need Wkhtmltopdf to print a pdf version of the reports.', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
            ],
            orelse=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Constant(value='Will use the Wkhtmltopdf binary at %s', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Name(id='_get_wkhtmltopdf_bin', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='out', ctx=Store()),
                                Name(id='err', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='process', ctx=Load()),
                            attr='communicate',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='search',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value=b'([0-9.]+)', kind=None),
                            Name(id='out', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='match', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='version', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ascii', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='LooseVersion', ctx=Load()),
                                    args=[Name(id='version', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Lt()],
                                comparators=[
                                    Call(
                                        func=Name(id='LooseVersion', ctx=Load()),
                                        args=[Constant(value='0.12.0', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Upgrade Wkhtmltopdf to (at least) 0.12.0', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='wkhtmltopdf_state', ctx=Store())],
                                    value=Constant(value='upgrade', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='wkhtmltopdf_state', ctx=Store())],
                                    value=Constant(value='ok', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='LooseVersion', ctx=Load()),
                                    args=[Name(id='version', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[GtE()],
                                comparators=[
                                    Call(
                                        func=Name(id='LooseVersion', ctx=Load()),
                                        args=[Constant(value='0.12.2', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='wkhtmltopdf_dpi_zoom_ratio', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='config', ctx=Load()),
                                    slice=Constant(value='workers', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='You need to start Odoo with at least two workers to print a pdf version of the reports.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='wkhtmltopdf_state', ctx=Store())],
                                    value=Constant(value='workers', kind=None),
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Wkhtmltopdf seems to be broken.', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='wkhtmltopdf_state', ctx=Store())],
                            value=Constant(value='broken', kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            finalbody=[],
        ),
        ClassDef(
            name='IrActionsReport',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.actions.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Report Action', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.actions.actions', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_table', ctx=Store())],
                    value=Constant(value='ir_act_report_xml', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sequence', ctx=Store())],
                    value=Constant(value='ir_actions_id_seq', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='ir.actions.report', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='binding_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='report', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Model Name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Model', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_model_id', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_model_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='qweb-html', kind=None),
                                            Constant(value='HTML', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='qweb-pdf', kind=None),
                                            Constant(value='PDF', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='qweb-text', kind=None),
                                            Constant(value='Text', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='qweb-pdf', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The type of the report that will be rendered, each one having its own rendering method. HTML means the report will be opened directly in your browser PDF means the report will be rendered using Wkhtmltopdf and downloaded by the user.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Template Name', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_file', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Report File', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The path to the main report file (depending on Report Type) or empty if the content is in another field', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='groups_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.groups', kind=None),
                            Constant(value='res_groups_report_rel', kind=None),
                            Constant(value='uid', kind=None),
                            Constant(value='gid', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Groups', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='multi', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='On Multiple Doc.', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If set to true, the action will not be displayed on the right toolbar of a form view.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='paperformat_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='report.paperformat', kind=None),
                            Constant(value='Paper Format', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='print_report_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Printed Report Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="This is the filename of the report going to download. Keep empty to not change the report filename. You can use a python expression with the 'object' and 'time' variables.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='attachment_use', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Reload from Attachment', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If enabled, then the second time the user prints with same attachment name, it returns the previous report.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='attachment', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Save as Attachment Prefix', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This is the filename of the attachment used to store the printing result. Keep empty to not save the printed reports. You can use a python expression with the object and time variables.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_model_id',
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
                        For(
                            target=Name(id='action', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='model_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='ir.model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='action', ctx=Load()),
                                                    attr='model',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='model', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_model_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
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
                            targets=[Name(id='ir_model_ids', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='names', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.model', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='name_search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='operator',
                                                value=Name(id='operator', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ir_model_ids', ctx=Store())],
                                    value=ListComp(
                                        elt=Subscript(
                                            value=Name(id='n', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='n', ctx=Store()),
                                                iter=Name(id='names', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='value', ctx=Load()),
                                            Name(id='Iterable', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='ir_model_ids', ctx=Store())],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='value', ctx=Load()),
                                                            Name(id='int', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='isinstance', ctx=Load()),
                                                            args=[
                                                                Name(id='value', ctx=Load()),
                                                                Name(id='bool', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ir_model_ids', ctx=Store())],
                                                    value=List(
                                                        elts=[Name(id='value', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='ir_model_ids', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='operator', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='operator', ctx=Load()),
                                            ops=[In()],
                                            comparators=[Name(id='NEGATIVE_TERM_OPERATORS', ctx=Load())],
                                        ),
                                        body=Constant(value='not in', kind=None),
                                        orelse=Constant(value='in', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ir_model', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.model', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ir_model_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='model', kind=None),
                                                    Name(id='operator', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='ir_model', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='model', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='value', ctx=Load()),
                                                    Name(id='bool', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='model', kind=None),
                                                            Name(id='operator', ctx=Load()),
                                                            Name(id='value', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Name(id='FALSE_DOMAIN', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_readable_fields',
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
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='_get_readable_fields',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=BitOr(),
                                right=Set(
                                    elts=[
                                        Constant(value='report_name', kind=None),
                                        Constant(value='report_type', kind=None),
                                        Constant(value='target', kind=None),
                                        Constant(value='context', kind=None),
                                        Constant(value='data', kind=None),
                                        Constant(value='close_on_report_download', kind=None),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='associated_view',
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
                            value=Constant(value='Used in the ir.actions.report form view in order to search naively after the view(s)\n        used in the rendering.\n        ', kind=None),
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
                            targets=[Name(id='action_ref', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.action_ui_view', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='action_ref', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='report_name',
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='.', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='action_data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='action_ref', ctx=Load()),
                                        attr='read',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action_data', ctx=Load()),
                                    slice=Constant(value='domain', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='ilike', kind=None),
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='report_name',
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='.', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='type', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='qweb', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='action_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create_action',
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
                            value=Constant(value=' Create a contextual action for each report. ', kind=None),
                        ),
                        For(
                            target=Name(id='report', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
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
                                                slice=Constant(value='ir.model', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='report', ctx=Load()),
                                                attr='model',
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
                                            value=Name(id='report', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='binding_model_id', kind=None),
                                                    Constant(value='binding_type', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='report', kind=None),
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
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink_action',
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
                            value=Constant(value=' Remove the contextual actions created for the reports. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='write', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_exception',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='binding_model_id', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='binding_model_id', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_retrieve_stream_from_attachment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attachment', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        ImportFrom(
                            module='PIL',
                            names=[alias(name='PdfImagePlugin', asname=None)],
                            level=0,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='attachment', ctx=Load()),
                                        attr='mimetype',
                                        ctx=Load(),
                                    ),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='image', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='stream', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64decode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='datas',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='img', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='open',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stream', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='output_stream', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='img', ctx=Load()),
                                                    attr='convert',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='RGB', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='output_stream', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='format',
                                                value=Constant(value='pdf', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Return(
                                    value=Name(id='output_stream', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='decodebytes',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='datas',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='retrieve_attachment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Retrieve an attachment for a specific record.\n\n        :param record: The record owning of the attachment.\n        :param attachment_name: The optional name of the attachment.\n        :return: A recordset of length <=1 or None\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attachment_name', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='attachment',
                                    ctx=Load(),
                                ),
                                body=Call(
                                    func=Name(id='safe_eval', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='attachment',
                                            ctx=Load(),
                                        ),
                                        Dict(
                                            keys=[
                                                Constant(value='object', kind=None),
                                                Constant(value='time', kind=None),
                                            ],
                                            values=[
                                                Name(id='record', ctx=Load()),
                                                Name(id='time', ctx=Load()),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='attachment_name', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
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
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='attachment_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='model',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_postprocess_pdf_report',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='buffer', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Hook to handle post processing during the pdf report generation.\n        The basic behavior consists to create a new attachment containing the pdf\n        base64 encoded.\n\n        :param record_id: The record that will own the attachment.\n        :param pdf_content: The optional name content of the file to avoid reading both times.\n        :return: A modified buffer if the previous one has been modified, None otherwise.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attachment_name', ctx=Store())],
                            value=Call(
                                func=Name(id='safe_eval', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='attachment',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='object', kind=None),
                                            Constant(value='time', kind=None),
                                        ],
                                        values=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='time', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='attachment_name', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='attachment_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='raw', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='type', kind=None),
                                ],
                                values=[
                                    Name(id='attachment_name', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='buffer', ctx=Load()),
                                            attr='getvalue',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='model',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='binary', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.attachment', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='attachment_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AccessError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Cannot save PDF report %r as attachment', kind=None),
                                                    Subscript(
                                                        value=Name(id='attachment_vals', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='The PDF document %s is now saved in the database', kind=None),
                                            Subscript(
                                                value=Name(id='attachment_vals', ctx=Load()),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='buffer', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_wkhtmltopdf_state',
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
                            value=Constant(value='Get the current state of wkhtmltopdf: install, ok, upgrade, workers or broken.\n        * install: Starting state.\n        * upgrade: The binary is an older version (< 0.12.0).\n        * ok: A binary was found with a recent version (>= 0.12.0).\n        * workers: Not enough workers found to perform the pdf rendering process (< 2 workers).\n        * broken: A binary was found but not responding.\n\n        :return: wkhtmltopdf_state\n        ', kind=None),
                        ),
                        Return(
                            value=Name(id='wkhtmltopdf_state', ctx=Load()),
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
                    name='get_paperformat',
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
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paperformat_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='paperformat_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_build_wkhtmltopdf_args',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='paperformat_id', annotation=None, type_comment=None),
                            arg(arg='landscape', annotation=None, type_comment=None),
                            arg(arg='specific_paperformat_args', annotation=None, type_comment=None),
                            arg(arg='set_viewport_size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Build arguments understandable by wkhtmltopdf bin.\n\n        :param paperformat_id: A report.paperformat record.\n        :param landscape: Force the report orientation to be landscape.\n        :param specific_paperformat_args: A dictionary containing prioritized wkhtmltopdf arguments.\n        :param set_viewport_size: Enable a viewport sized '1024x1280' or '1280x1024' depending of landscape arg.\n        :return: A list of string representing the wkhtmltopdf process command args.\n        ", kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='landscape', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Name(id='specific_paperformat_args', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='specific_paperformat_args', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='data-report-landscape', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='landscape', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='specific_paperformat_args', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='data-report-landscape', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='command_args', ctx=Store())],
                            value=List(
                                elts=[Constant(value='--disable-local-file-access', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='set_viewport_size', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='command_args', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='--viewport-size', kind=None),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='landscape', ctx=Load()),
                                                                    Constant(value='1024x1280', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='1280x1024', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                If(
                                    test=Name(id='request', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='--cookie', kind=None),
                                                            Constant(value='session_id', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='session',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='sid',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AttributeError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='command_args', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='--quiet', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='paperformat_id', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='paperformat_id', ctx=Load()),
                                                attr='format',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='paperformat_id', ctx=Load()),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='custom', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='--page-size', kind=None),
                                                            Attribute(
                                                                value=Name(id='paperformat_id', ctx=Load()),
                                                                attr='format',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='paperformat_id', ctx=Load()),
                                                attr='page_height',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='paperformat_id', ctx=Load()),
                                                attr='page_width',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='paperformat_id', ctx=Load()),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='custom', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='--page-width', kind=None),
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='paperformat_id', ctx=Load()),
                                                                            attr='page_width',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value='mm', kind=None),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='--page-height', kind=None),
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='paperformat_id', ctx=Load()),
                                                                            attr='page_height',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value='mm', kind=None),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='specific_paperformat_args', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='specific_paperformat_args', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='data-report-margin-top', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='--margin-top', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='specific_paperformat_args', ctx=Load()),
                                                                        slice=Constant(value='data-report-margin-top', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
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
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='--margin-top', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='paperformat_id', ctx=Load()),
                                                                        attr='margin_top',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='dpi', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='specific_paperformat_args', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='specific_paperformat_args', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='data-report-dpi', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='dpi', ctx=Store())],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='specific_paperformat_args', ctx=Load()),
                                                        slice=Constant(value='data-report-dpi', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='paperformat_id', ctx=Load()),
                                                attr='dpi',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='os', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='nt', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Call(
                                                                    func=Name(id='int', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='paperformat_id', ctx=Load()),
                                                                            attr='dpi',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ops=[LtE()],
                                                                comparators=[Constant(value=95, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='Generating PDF on Windows platform require DPI >= 96. Using 96 instead.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='dpi', ctx=Store())],
                                                            value=Constant(value=96, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='dpi', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='paperformat_id', ctx=Load()),
                                                                attr='dpi',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Name(id='dpi', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='--dpi', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='dpi', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Name(id='wkhtmltopdf_dpi_zoom_ratio', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='command_args', ctx=Load()),
                                                            attr='extend',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='--zoom', kind=None),
                                                                    Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Constant(value=96.0, kind=None),
                                                                                op=Div(),
                                                                                right=Name(id='dpi', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='specific_paperformat_args', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='specific_paperformat_args', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='data-report-header-spacing', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='--header-spacing', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='specific_paperformat_args', ctx=Load()),
                                                                        slice=Constant(value='data-report-header-spacing', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='paperformat_id', ctx=Load()),
                                                attr='header_spacing',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='command_args', ctx=Load()),
                                                            attr='extend',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='--header-spacing', kind=None),
                                                                    Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='paperformat_id', ctx=Load()),
                                                                                attr='header_spacing',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='command_args', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='--margin-left', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='paperformat_id', ctx=Load()),
                                                                attr='margin_left',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='command_args', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='--margin-bottom', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='paperformat_id', ctx=Load()),
                                                                attr='margin_bottom',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='command_args', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='--margin-right', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='paperformat_id', ctx=Load()),
                                                                attr='margin_right',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='landscape', ctx=Load()),
                                            ),
                                            Attribute(
                                                value=Name(id='paperformat_id', ctx=Load()),
                                                attr='orientation',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='--orientation', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='paperformat_id', ctx=Load()),
                                                                        attr='orientation',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='paperformat_id', ctx=Load()),
                                        attr='header_line',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Constant(value='--header-line', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='paperformat_id', ctx=Load()),
                                        attr='disable_shrinking',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='command_args', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Constant(value='--disable-smart-shrinking', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='landscape', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='command_args', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='--orientation', kind=None),
                                                    Constant(value='landscape', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='command_args', ctx=Load()),
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
                    name='_prepare_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='html', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Divide and recreate the header/footer html by merging all found in html.\n        The bodies are extracted and added to a list. Then, extract the specific_paperformat_args.\n        The idea is to put all headers/footers together. Then, we will use a javascript trick\n        (see minimal_layout template) to set the right header/footer during the processing of wkhtmltopdf.\n        This allows the computation of multiple reports in a single call to wkhtmltopdf.\n\n        :param html: The html rendered by render_qweb_html.\n        :type: bodies: list of string representing each one a html body.\n        :type header: string representing the html header.\n        :type footer: string representing the html footer.\n        :type specific_paperformat_args: dictionary of prioritized paperformat values.\n        :return: bodies, header, footer, specific_paperformat_args\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='IrConfig', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='layout', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='web.minimal_layout', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='layout', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='layout', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_view_id',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='web.minimal_layout', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_url', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrConfig', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='report.url', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='layout', ctx=Load()),
                                            attr='get_base_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='root', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='lxml', ctx=Load()),
                                        attr='html',
                                        ctx=Load(),
                                    ),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='html', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='match_klass', ctx=Store())],
                            value=Constant(value="//div[contains(concat(' ', normalize-space(@class), ' '), ' {} ')]", kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='header_node', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='div', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='id',
                                        value=Constant(value='minimal_layout_report_headers', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='footer_node', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='div', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='id',
                                        value=Constant(value='minimal_layout_report_footers', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bodies', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='body_parent', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='root', ctx=Load()),
                                        attr='xpath',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='//main', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='node', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='root', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='match_klass', ctx=Load()),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='header', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='body_parent', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='getparent',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='getparent',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='remove',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='node', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='header_node', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='node', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='node', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='root', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='match_klass', ctx=Load()),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='footer', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='body_parent', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='getparent',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='getparent',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='remove',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='node', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='footer_node', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='node', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='node', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='root', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='match_klass', ctx=Load()),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='article', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='layout_with_lang', ctx=Store())],
                                    value=Name(id='layout', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='data-oe-lang', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='layout_with_lang', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='layout_with_lang', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='lang',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='node', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='data-oe-lang', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='layout_with_lang', ctx=Load()),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='subst', kind=None),
                                                    Constant(value='body', kind=None),
                                                    Constant(value='base_url', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Call(
                                                        func=Name(id='Markup', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='lxml', ctx=Load()),
                                                                        attr='html',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='tostring',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='node', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='encoding',
                                                                        value=Constant(value='unicode', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Name(id='base_url', ctx=Load()),
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
                                            value=Name(id='bodies', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='body', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='data-oe-model', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='model',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='data-oe-id', kind=None),
                                                                    Constant(value=0, kind=None),
                                                                ],
                                                                keywords=[],
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
                                                    value=Name(id='res_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=None, kind=None)],
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='bodies', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='lxml', ctx=Load()),
                                                            attr='html',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tostring',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='c', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg='encoding',
                                                            value=Constant(value='unicode', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='c', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='body_parent', ctx=Load()),
                                                                attr='getchildren',
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
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='bodies', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='body', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='specific_paperformat_args', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attribute', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='root', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='attribute', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='data-report-', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='specific_paperformat_args', ctx=Load()),
                                                    slice=Subscript(
                                                        value=Name(id='attribute', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='attribute', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
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
                            targets=[Name(id='header', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='layout', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='subst', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='base_url', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Name(id='Markup', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='lxml', ctx=Load()),
                                                                attr='html',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tostring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='header_node', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='encoding',
                                                                value=Constant(value='unicode', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='base_url', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='footer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='layout', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='subst', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='base_url', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Name(id='Markup', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='lxml', ctx=Load()),
                                                                attr='html',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tostring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='footer_node', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='encoding',
                                                                value=Constant(value='unicode', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='base_url', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='bodies', ctx=Load()),
                                    Name(id='res_ids', ctx=Load()),
                                    Name(id='header', ctx=Load()),
                                    Name(id='footer', ctx=Load()),
                                    Name(id='specific_paperformat_args', ctx=Load()),
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
                    name='_run_wkhtmltopdf',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bodies', annotation=None, type_comment=None),
                            arg(arg='header', annotation=None, type_comment=None),
                            arg(arg='footer', annotation=None, type_comment=None),
                            arg(arg='landscape', annotation=None, type_comment=None),
                            arg(arg='specific_paperformat_args', annotation=None, type_comment=None),
                            arg(arg='set_viewport_size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Execute wkhtmltopdf as a subprocess in order to convert html given in input into a pdf\n        document.\n\n        :param list[str] bodies: The html bodies of the report, one per page.\n        :param str header: The html header of the report containing all headers.\n        :param str footer: The html footer of the report containing all footers.\n        :param landscape: Force the pdf to be rendered under a landscape format.\n        :param specific_paperformat_args: dict of prioritized paperformat arguments.\n        :param set_viewport_size: Enable a viewport sized '1024x1280' or '1280x1024' depending of landscape arg.\n        :return: Content of the pdf as bytes\n        :rtype: bytes\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='paperformat_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_paperformat',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='command_args', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_build_wkhtmltopdf_args',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='paperformat_id', ctx=Load()),
                                    Name(id='landscape', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='specific_paperformat_args',
                                        value=Name(id='specific_paperformat_args', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='set_viewport_size',
                                        value=Name(id='set_viewport_size', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='files_command_args', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='temporary_files', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='header', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='head_file_fd', ctx=Store()),
                                                Name(id='head_file_path', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tempfile', ctx=Load()),
                                            attr='mkstemp',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='suffix',
                                                value=Constant(value='.html', kind=None),
                                            ),
                                            keyword(
                                                arg='prefix',
                                                value=Constant(value='report.header.tmp.', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='closing', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='fdopen',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='head_file_fd', ctx=Load()),
                                                            Constant(value='wb', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='head_file', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='head_file', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='header', ctx=Load()),
                                                            attr='encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='temporary_files', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='head_file_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='files_command_args', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='--header-html', kind=None),
                                                    Name(id='head_file_path', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='footer', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='foot_file_fd', ctx=Store()),
                                                Name(id='foot_file_path', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tempfile', ctx=Load()),
                                            attr='mkstemp',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='suffix',
                                                value=Constant(value='.html', kind=None),
                                            ),
                                            keyword(
                                                arg='prefix',
                                                value=Constant(value='report.footer.tmp.', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='closing', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='fdopen',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='foot_file_fd', ctx=Load()),
                                                            Constant(value='wb', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='foot_file', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='foot_file', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='footer', ctx=Load()),
                                                            attr='encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='temporary_files', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='foot_file_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='files_command_args', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='--footer-html', kind=None),
                                                    Name(id='foot_file_path', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='paths', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='i', ctx=Store()),
                                    Name(id='body', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='bodies', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='prefix', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s%d.', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Constant(value='report.body.tmp.', kind=None),
                                                Name(id='i', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='body_file_fd', ctx=Store()),
                                                Name(id='body_file_path', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tempfile', ctx=Load()),
                                            attr='mkstemp',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='suffix',
                                                value=Constant(value='.html', kind=None),
                                            ),
                                            keyword(
                                                arg='prefix',
                                                value=Name(id='prefix', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='closing', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='fdopen',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='body_file_fd', ctx=Load()),
                                                            Constant(value='wb', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='body_file', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_file', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='body', ctx=Load()),
                                                            attr='encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='paths', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='body_file_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='temporary_files', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='body_file_path', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='pdf_report_fd', ctx=Store()),
                                        Name(id='pdf_report_path', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tempfile', ctx=Load()),
                                    attr='mkstemp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='suffix',
                                        value=Constant(value='.pdf', kind=None),
                                    ),
                                    keyword(
                                        arg='prefix',
                                        value=Constant(value='report.tmp.', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[Name(id='pdf_report_fd', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='temporary_files', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='pdf_report_path', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='wkhtmltopdf', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=List(
                                                        elts=[
                                                            Call(
                                                                func=Name(id='_get_wkhtmltopdf_bin', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Name(id='command_args', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='files_command_args', ctx=Load()),
                                            ),
                                            op=Add(),
                                            right=Name(id='paths', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=List(
                                            elts=[Name(id='pdf_report_path', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='process', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='Popen',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='wkhtmltopdf', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='stdout',
                                                value=Attribute(
                                                    value=Name(id='subprocess', ctx=Load()),
                                                    attr='PIPE',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='stderr',
                                                value=Attribute(
                                                    value=Name(id='subprocess', ctx=Load()),
                                                    attr='PIPE',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='out', ctx=Store()),
                                                Name(id='err', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='process', ctx=Load()),
                                            attr='communicate',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='process', ctx=Load()),
                                            attr='returncode',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='process', ctx=Load()),
                                                    attr='returncode',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=11, kind=None),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='message', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Wkhtmltopdf failed (error code: %s). Memory limit too low or maximum file number of subprocess reached. Message : %s', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='message', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Wkhtmltopdf failed (error code: %s). Message: %s', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='message', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='process', ctx=Load()),
                                                        attr='returncode',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='err', ctx=Load()),
                                                        slice=Slice(
                                                            lower=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1000, kind=None),
                                                            ),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='message', ctx=Load()),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='process', ctx=Load()),
                                                                            attr='returncode',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='err', ctx=Load()),
                                                                    slice=Slice(
                                                                        lower=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Constant(value=1000, kind=None),
                                                                        ),
                                                                        upper=None,
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Name(id='err', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='wkhtmltopdf: %s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='err', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[Raise(exc=None, cause=None)],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='pdf_report_path', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='pdf_document', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='pdf_content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='pdf_document', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='temporary_file', ctx=Store()),
                            iter=Name(id='temporary_files', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='unlink',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='temporary_file', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='OSError', ctx=Load()),
                                                    Name(id='IOError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Error when trying to remove file %s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='temporary_file', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='pdf_content', ctx=Load()),
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
                    name='_get_report_from_name',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='report_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Get the first record of ir.actions.report having the ``report_name`` as value for\n        the field report_name.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='report_obj', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.actions.report', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='conditions', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='report_name', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='report_name', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='context_get',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='report_obj', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='context', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='conditions', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
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
                    name='barcode',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='barcode_type', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='width', annotation=None, type_comment=None),
                            arg(arg='height', annotation=None, type_comment=None),
                            arg(arg='humanreadable', annotation=None, type_comment=None),
                            arg(arg='quiet', annotation=None, type_comment=None),
                            arg(arg='mask', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=600, kind=None),
                            Constant(value=100, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=1, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='barcode_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='UPCA', kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='value', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=11, kind=None),
                                                    Constant(value=12, kind=None),
                                                    Constant(value=13, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='barcode_type', ctx=Store())],
                                    value=Constant(value='EAN13', kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='value', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=11, kind=None),
                                                    Constant(value=12, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='0%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='value', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='barcode_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='auto', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='symbology_guess', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value=8, kind=None),
                                                    Constant(value=13, kind=None),
                                                ],
                                                values=[
                                                    Constant(value='EAN8', kind=None),
                                                    Constant(value='EAN13', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='barcode_type', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='symbology_guess', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='Code128', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='width', ctx=Store()),
                                                Name(id='height', ctx=Store()),
                                                Name(id='humanreadable', ctx=Store()),
                                                Name(id='quiet', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='width', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='height', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='humanreadable', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='quiet', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='bar_border', ctx=Store())],
                                    value=Constant(value=4, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='barcode_type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='QR', kind=None)],
                                            ),
                                            Name(id='quiet', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='bar_border', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='barcode', ctx=Store())],
                                    value=Call(
                                        func=Name(id='createBarcodeDrawing', ctx=Load()),
                                        args=[Name(id='barcode_type', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='value',
                                                value=Name(id='value', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='format',
                                                value=Constant(value='png', kind=None),
                                            ),
                                            keyword(
                                                arg='width',
                                                value=Name(id='width', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='height',
                                                value=Name(id='height', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='humanReadable',
                                                value=Name(id='humanreadable', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='quiet',
                                                value=Name(id='quiet', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='barBorder',
                                                value=Name(id='bar_border', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='mask', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='available_masks', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_available_barcode_masks',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='mask_to_apply', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='available_masks', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='mask', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='mask_to_apply', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='mask_to_apply', ctx=Load()),
                                                        args=[
                                                            Name(id='width', ctx=Load()),
                                                            Name(id='height', ctx=Load()),
                                                            Name(id='barcode', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='barcode', ctx=Load()),
                                            attr='asString',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='png', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='ValueError', ctx=Load()),
                                            Name(id='AttributeError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='barcode_type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='Code128', kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValueError', ctx=Load()),
                                                        args=[Constant(value='Cannot convert into barcode.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='barcode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Code128', kind=None),
                                                            Name(id='value', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='width',
                                                                value=Name(id='width', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='height',
                                                                value=Name(id='height', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='humanreadable',
                                                                value=Name(id='humanreadable', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='quiet',
                                                                value=Name(id='quiet', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
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
                    name='get_available_barcode_masks',
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
                            value=Constant(value=' Hook for extension.\n        This function returns the available QR-code masks, in the form of a\n        list of (code, mask_function) elements, where code is a string identifying\n        the mask uniquely, and mask_function is a function returning a reportlab\n        Drawing object with the result of the mask, and taking as parameters:\n            - width of the QR-code, in pixels\n            - height of the QR-code, in pixels\n            - reportlab Drawing object containing the barcode to apply the mask on\n        ', kind=None),
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
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
                    name='_render_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Allow to render a QWeb template python-side. This function returns the 'ir.ui.view'\n        render but embellish it with some variables/methods used in reports.\n        :param values: additional methods/variables used in the rendering\n        :returns: html representation of the template\n        :rtype: bytes\n        ", kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='values', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='inherit_branding',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='request', ctx=Load()),
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='request', ctx=Load()),
                                            Constant(value='website', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='website',
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='website', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='website',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='context', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='context', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='translatable',
                                                        value=Compare(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Name(id='context', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='lang', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            ops=[NotEq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='request', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='ir.http', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='_get_default_lang',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='code',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='view_obj', ctx=Store())],
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
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='time',
                                        value=Name(id='time', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='context_timestamp',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='t', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context_timestamp',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='tz',
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='tz',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='t', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='user',
                                        value=Name(id='user', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='res_company',
                                        value=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='website',
                                        value=Name(id='website', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='web_base_url',
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
                                                            slice=Constant(value='ir.config_parameter', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='get_param',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='web.base.url', kind=None)],
                                            keywords=[
                                                keyword(
                                                    arg='default',
                                                    value=Constant(value='', kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view_obj', ctx=Load()),
                                            attr='_render_template',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='template', ctx=Load()),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='encode',
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
                FunctionDef(
                    name='_post_pdf',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='save_in_attachment', annotation=None, type_comment=None),
                            arg(arg='pdf_content', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Merge the existing attachments by adding one by one the content of the attachments\n        and then, we add the pdf_content if exists. Create the attachments for each record individually\n        if required.\n\n        :param save_in_attachment: The retrieved attachments as map record.id -> attachment_id.\n        :param pdf_content: The pdf content newly generated by wkhtmltopdf.\n        :param res_ids: the ids of record to allow postprocessing.\n        :return: The pdf content of the merged pdf.\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='close_streams',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='streams', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='stream', ctx=Store()),
                                    iter=Name(id='streams', ctx=Load()),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='stream', ctx=Load()),
                                                            attr='close',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
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
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='save_in_attachment', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='pdf_content', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Call(
                                                    func=Name(id='list', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='save_in_attachment', ctx=Load()),
                                                                attr='values',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='getvalue',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='streams', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='pdf_content', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='pdf_content_stream', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pdf_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='record_map', ctx=Store())],
                                    value=DictComp(
                                        key=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        value=Name(id='r', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='r', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='model',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        ListComp(
                                                            elt=Name(id='res_id', ctx=Load()),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='res_id', ctx=Store()),
                                                                    iter=Name(id='res_ids', ctx=Load()),
                                                                    ifs=[Name(id='res_id', ctx=Load())],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='record_map', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='attachment',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='streams', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='pdf_content_stream', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='res_ids', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='res_ids', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='record_map', ctx=Load())],
                                                            ),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Compare(
                                                                    left=Subscript(
                                                                        value=Name(id='res_ids', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[In()],
                                                                    comparators=[Name(id='save_in_attachment', ctx=Load())],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='new_stream', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_postprocess_pdf_report',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='record_map', ctx=Load()),
                                                                        slice=Subscript(
                                                                            value=Name(id='res_ids', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='pdf_content_stream', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='new_stream', ctx=Load()),
                                                                    Compare(
                                                                        left=Name(id='new_stream', ctx=Load()),
                                                                        ops=[NotEq()],
                                                                        comparators=[Name(id='pdf_content_stream', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Name(id='close_streams', ctx=Load()),
                                                                        args=[
                                                                            List(
                                                                                elts=[Name(id='pdf_content_stream', ctx=Load())],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='pdf_content_stream', ctx=Store())],
                                                                    value=Name(id='new_stream', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='streams', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='pdf_content_stream', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='reader', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='PdfFileReader', ctx=Load()),
                                                        args=[Name(id='pdf_content_stream', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='root', ctx=Store())],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='reader', ctx=Load()),
                                                            attr='trailer',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='/Root', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Constant(value='/Outlines', kind=None),
                                                                ops=[In()],
                                                                comparators=[Name(id='root', ctx=Load())],
                                                            ),
                                                            Compare(
                                                                left=Constant(value='/First', kind=None),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Subscript(
                                                                        value=Name(id='root', ctx=Load()),
                                                                        slice=Constant(value='/Outlines', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='outlines_pages', ctx=Store())],
                                                            value=List(elts=[], ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='node', ctx=Store())],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='root', ctx=Load()),
                                                                    slice=Constant(value='/Outlines', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='/First', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        While(
                                                            test=Constant(value=True, kind=None),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='outlines_pages', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Subscript(
                                                                                    value=Subscript(
                                                                                        value=Name(id='root', ctx=Load()),
                                                                                        slice=Constant(value='/Dests', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Subscript(
                                                                                        value=Name(id='node', ctx=Load()),
                                                                                        slice=Constant(value='/Dest', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Constant(value='/Next', kind=None),
                                                                        ops=[NotIn()],
                                                                        comparators=[Name(id='node', ctx=Load())],
                                                                    ),
                                                                    body=[Break()],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='node', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Name(id='node', ctx=Load()),
                                                                        slice=Constant(value='/Next', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='outlines_pages', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='sorted', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='set', ctx=Load()),
                                                                        args=[Name(id='outlines_pages', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assert(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='outlines_pages', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Call(
                                                                        func=Name(id='len', ctx=Load()),
                                                                        args=[Name(id='res_ids', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            msg=None,
                                                        ),
                                                        Assert(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Name(id='outlines_pages', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            msg=None,
                                                        ),
                                                        For(
                                                            target=Tuple(
                                                                elts=[
                                                                    Name(id='i', ctx=Store()),
                                                                    Name(id='num', ctx=Store()),
                                                                ],
                                                                ctx=Store(),
                                                            ),
                                                            iter=Call(
                                                                func=Name(id='enumerate', ctx=Load()),
                                                                args=[Name(id='outlines_pages', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='to', ctx=Store())],
                                                                    value=IfExp(
                                                                        test=Compare(
                                                                            left=BinOp(
                                                                                left=Name(id='i', ctx=Load()),
                                                                                op=Add(),
                                                                                right=Constant(value=1, kind=None),
                                                                            ),
                                                                            ops=[Lt()],
                                                                            comparators=[
                                                                                Call(
                                                                                    func=Name(id='len', ctx=Load()),
                                                                                    args=[Name(id='outlines_pages', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        body=Subscript(
                                                                            value=Name(id='outlines_pages', ctx=Load()),
                                                                            slice=BinOp(
                                                                                left=Name(id='i', ctx=Load()),
                                                                                op=Add(),
                                                                                right=Constant(value=1, kind=None),
                                                                            ),
                                                                            ctx=Load(),
                                                                        ),
                                                                        orelse=Attribute(
                                                                            value=Name(id='reader', ctx=Load()),
                                                                            attr='numPages',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='attachment_writer', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='PdfFileWriter', ctx=Load()),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                For(
                                                                    target=Name(id='j', ctx=Store()),
                                                                    iter=Call(
                                                                        func=Name(id='range', ctx=Load()),
                                                                        args=[
                                                                            Name(id='num', ctx=Load()),
                                                                            Name(id='to', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='attachment_writer', ctx=Load()),
                                                                                    attr='addPage',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='reader', ctx=Load()),
                                                                                            attr='getPage',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='j', ctx=Load())],
                                                                                        keywords=[],
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
                                                                    targets=[Name(id='stream', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='io', ctx=Load()),
                                                                            attr='BytesIO',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='attachment_writer', ctx=Load()),
                                                                            attr='write',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='stream', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Subscript(
                                                                                value=Name(id='res_ids', ctx=Load()),
                                                                                slice=Name(id='i', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Compare(
                                                                                left=Subscript(
                                                                                    value=Name(id='res_ids', ctx=Load()),
                                                                                    slice=Name(id='i', ctx=Load()),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[NotIn()],
                                                                                comparators=[Name(id='save_in_attachment', ctx=Load())],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='new_stream', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_postprocess_pdf_report',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='record_map', ctx=Load()),
                                                                                        slice=Subscript(
                                                                                            value=Name(id='res_ids', ctx=Load()),
                                                                                            slice=Name(id='i', ctx=Load()),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='stream', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Name(id='new_stream', ctx=Load()),
                                                                                    Compare(
                                                                                        left=Name(id='new_stream', ctx=Load()),
                                                                                        ops=[NotEq()],
                                                                                        comparators=[Name(id='stream', ctx=Load())],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Name(id='close_streams', ctx=Load()),
                                                                                        args=[
                                                                                            List(
                                                                                                elts=[Name(id='stream', ctx=Load())],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='stream', ctx=Store())],
                                                                                    value=Name(id='new_stream', ctx=Load()),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='streams', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='stream', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='close_streams', ctx=Load()),
                                                                args=[
                                                                    List(
                                                                        elts=[Name(id='pdf_content_stream', ctx=Load())],
                                                                        ctx=Load(),
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
                                                                    value=Name(id='streams', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='pdf_content_stream', ctx=Load())],
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
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='attachment_use',
                                ctx=Load(),
                            ),
                            body=[
                                For(
                                    target=Name(id='stream', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='save_in_attachment', ctx=Load()),
                                            attr='values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='streams', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='stream', ctx=Load())],
                                                keywords=[],
                                            ),
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
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='streams', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='streams', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='getvalue',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='result', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_merge_pdfs',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='streams', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='utils', ctx=Load()),
                                                attr='PdfReadError',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='One of the documents, you try to merge is encrypted', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
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
                        Expr(
                            value=Call(
                                func=Name(id='close_streams', ctx=Load()),
                                args=[Name(id='streams', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_unreadable_pdfs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='streams', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='unreadable_streams', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='stream', ctx=Store()),
                            iter=Name(id='streams', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='writer', ctx=Store())],
                                    value=Call(
                                        func=Name(id='PdfFileWriter', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result_stream', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='reader', ctx=Store())],
                                            value=Call(
                                                func=Name(id='PdfFileReader', ctx=Load()),
                                                args=[Name(id='stream', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='writer', ctx=Load()),
                                                    attr='appendPagesFromReader',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='reader', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='writer', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='result_stream', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='utils', ctx=Load()),
                                                attr='PdfReadError',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='unreadable_streams', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='stream', ctx=Load())],
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
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='unreadable_streams', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_raise_on_unreadable_pdfs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='streams', annotation=None, type_comment=None),
                            arg(arg='stream_record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='unreadable_pdfs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_unreadable_pdfs',
                                    ctx=Load(),
                                ),
                                args=[Name(id='streams', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='unreadable_pdfs', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='records', ctx=Store())],
                                    value=ListComp(
                                        elt=Attribute(
                                            value=Subscript(
                                                value=Name(id='stream_record', ctx=Load()),
                                                slice=Name(id='s', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='s', ctx=Store()),
                                                iter=Name(id='unreadable_pdfs', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='s', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='stream_record', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value="Odoo is unable to merge the PDFs attached to the following records:\n%s\n\nPlease exclude them from the selection to continue. It's possible to still retrieve those PDFs by selecting each of the affected records individually, which will avoid merging.", kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Constant(value='\n', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='records', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_merge_pdfs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='streams', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Name(id='PdfFileWriter', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='stream', ctx=Store()),
                            iter=Name(id='streams', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='reader', ctx=Store())],
                                    value=Call(
                                        func=Name(id='PdfFileReader', ctx=Load()),
                                        args=[Name(id='stream', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='appendPagesFromReader',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='reader', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result_stream', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='streams', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='result_stream', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='result_stream', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='result_stream', ctx=Load()),
                                    attr='getvalue',
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
                FunctionDef(
                    name='_render_qweb_pdf',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :rtype: bytes\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='data', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='report_type', kind=None),
                                    Constant(value='pdf', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='self_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='config',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='test_enable', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='config',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='test_file', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='force_report_rendering', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self_sudo', ctx=Load()),
                                            attr='_render_qweb_html',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res_ids', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='data',
                                                value=Name(id='data', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Name(id='config', ctx=Load()),
                                    slice=Constant(value='test_enable', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='context', ctx=Load()),
                                            slice=Constant(value='commit_assetsbundle', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='context', ctx=Load()),
                                    slice=Constant(value='debug', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='save_in_attachment', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stream_record', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='res_ids', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='Model', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self_sudo', ctx=Load()),
                                            attr='model',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='record_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Model', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='res_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='wk_record_ids', ctx=Store())],
                                    value=Name(id='Model', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self_sudo', ctx=Load()),
                                        attr='attachment',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='record_id', ctx=Store()),
                                            iter=Name(id='record_ids', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='attachment', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self_sudo', ctx=Load()),
                                                            attr='retrieve_attachment',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='record_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='attachment', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='stream', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self_sudo', ctx=Load()),
                                                                    attr='_retrieve_stream_from_attachment',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='attachment', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='save_in_attachment', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='record_id', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='stream', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='stream_record', ctx=Load()),
                                                                    slice=Name(id='stream', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='record_id', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='self_sudo', ctx=Load()),
                                                                    attr='attachment_use',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='attachment', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='wk_record_ids', ctx=Store()),
                                                            op=Add(),
                                                            value=Name(id='record_id', ctx=Load()),
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
                                        Assign(
                                            targets=[Name(id='wk_record_ids', ctx=Store())],
                                            value=Name(id='record_ids', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='res_ids', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='wk_record_ids', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='save_in_attachment', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='res_ids', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='The PDF report has been generated from attachments.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raise_on_unreadable_pdfs',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='save_in_attachment', ctx=Load()),
                                                    attr='values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='stream_record', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self_sudo', ctx=Load()),
                                                    attr='_post_pdf',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='save_in_attachment', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='pdf', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='get_wkhtmltopdf_state',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='install', kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Unable to find Wkhtmltopdf on this system. The PDF can not be created.', kind=None)],
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
                            targets=[Name(id='html', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self_sudo', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='context', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='_render_qweb_html',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='res_ids', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='data',
                                            value=Name(id='data', ctx=Load()),
                                        ),
                                    ],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='bodies', ctx=Store()),
                                        Name(id='html_ids', ctx=Store()),
                                        Name(id='header', ctx=Store()),
                                        Name(id='footer', ctx=Store()),
                                        Name(id='specific_paperformat_args', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self_sudo', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_prepare_html',
                                    ctx=Load(),
                                ),
                                args=[Name(id='html', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self_sudo', ctx=Load()),
                                        attr='attachment',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[Name(id='res_ids', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[Name(id='html_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value="The report's template '%s' is wrong, please contact your administrator. \n\nCan not separate file to save as attachment because the report's template does not contains the attributes 'data-oe-model' and 'data-oe-id' on the div with 'article' classname.", kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
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
                            targets=[Name(id='pdf_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_run_wkhtmltopdf',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bodies', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='header',
                                        value=Name(id='header', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='footer',
                                        value=Name(id='footer', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='landscape',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='context', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='landscape', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='specific_paperformat_args',
                                        value=Name(id='specific_paperformat_args', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='set_viewport_size',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='context', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='set_viewport_size', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='res_ids', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raise_on_unreadable_pdfs',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='save_in_attachment', ctx=Load()),
                                                    attr='values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='stream_record', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='The PDF report has been generated for model: %s, records %s.', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='self_sudo', ctx=Load()),
                                                            attr='model',
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='res_ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self_sudo', ctx=Load()),
                                                    attr='_post_pdf',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='save_in_attachment', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='pdf_content',
                                                        value=Name(id='pdf_content', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='res_ids',
                                                        value=Name(id='html_ids', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            Constant(value='pdf', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='pdf_content', ctx=Load()),
                                    Constant(value='pdf', kind=None),
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
                    name='_render_qweb_text',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='docids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :rtype: bytes\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='data', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='report_type', kind=None),
                                    Constant(value='text', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='__keep_empty_lines', kind=None),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_rendering_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='docids', ctx=Load()),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_render_template',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='report_name',
                                                ctx=Load(),
                                            ),
                                            Name(id='data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='text', kind=None),
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
                    name='_render_qweb_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='docids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='This method generates and returns html version of a report.\n\n        :rtype: bytes\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='data', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='report_type', kind=None),
                                    Constant(value='html', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_rendering_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='docids', ctx=Load()),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_render_template',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='report_name',
                                                ctx=Load(),
                                            ),
                                            Name(id='data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
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
                    name='_get_rendering_context_model',
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
                        Assign(
                            targets=[Name(id='report_model_name', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='report.%s', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='report_name',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='report_model_name', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_rendering_context',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='docids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='report_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_rendering_context_model',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='data', ctx=Load()),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='data', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='report_model', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='report_model', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='report_model', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=False, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='report_model', ctx=Load()),
                                                    attr='_get_report_values',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='docids', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='data',
                                                        value=Name(id='data', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='docs', ctx=Store())],
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
                                                        slice=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='model',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=False, kind=None)],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='docids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='doc_ids', kind=None),
                                                    Constant(value='doc_model', kind=None),
                                                    Constant(value='docs', kind=None),
                                                ],
                                                values=[
                                                    Name(id='docids', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='model',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='docs', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='is_html_empty', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='is_html_empty', ctx=Load()),
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
                    name='_render',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='res_ids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='report_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='report_type',
                                                ctx=Load(),
                                            ),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='-', kind=None),
                                    Constant(value='_', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='render_func', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='_render_', kind=None),
                                        op=Add(),
                                        right=Name(id='report_type', ctx=Load()),
                                    ),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='render_func', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='render_func', ctx=Load()),
                                args=[Name(id='res_ids', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='data',
                                        value=Name(id='data', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='report_action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='docids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='config', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return an action of type ir.actions.report.\n\n        :param docids: id/ids/browse record of the records to print (if not used, pass an empty list)\n        :param data:\n        :param bool config:\n        :rtype: bytes\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='context',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='docids', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='docids', ctx=Load()),
                                            Attribute(
                                                value=Name(id='models', ctx=Load()),
                                                attr='Model',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='active_ids', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='docids', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='docids', ctx=Load()),
                                                    Name(id='int', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='active_ids', ctx=Store())],
                                                    value=List(
                                                        elts=[Name(id='docids', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='docids', ctx=Load()),
                                                            Name(id='list', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='active_ids', ctx=Store())],
                                                            value=Name(id='docids', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='context', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='active_ids',
                                                value=Name(id='active_ids', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='report_action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='context', kind=None),
                                    Constant(value='data', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='report_name', kind=None),
                                    Constant(value='report_type', kind=None),
                                    Constant(value='report_file', kind=None),
                                    Constant(value='name', kind=None),
                                ],
                                values=[
                                    Name(id='context', ctx=Load()),
                                    Name(id='data', ctx=Load()),
                                    Constant(value='ir.actions.report', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='report_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='report_type',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='report_file',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='discard_logo_check', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='discard_logo_check', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='is_admin',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                            attr='external_report_layout_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Name(id='config', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='discard_logo_check', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='action', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.actions.actions', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_for_xml_id',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='web.action_base_document_layout_configurator', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ctx', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='context', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='py_ctx', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='ctx', ctx=Load()),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='ctx', ctx=Load())],
                                            keywords=[],
                                        ),
                                        orelse=Dict(keys=[], values=[]),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='report_action', ctx=Load()),
                                            slice=Constant(value='close_on_report_download', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='py_ctx', ctx=Load()),
                                            slice=Constant(value='report_action', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='report_action', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='context', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='py_ctx', ctx=Load()),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='action', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='report_action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
