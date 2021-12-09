Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='misc', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_account',
            names=[alias(name='TIMEOUT', asname=None)],
            level=0,
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
        ClassDef(
            name='GoogleDrive',
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
                    value=Constant(value='google.drive.config', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_google_scope',
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
                            targets=[Name(id='scope', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='GoogleDrive', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_google_scope',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%s https://spreadsheets.google.com/feeds', kind=None),
                                op=Mod(),
                                right=Name(id='scope', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write_config_formula',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attachment_id', annotation=None, type_comment=None),
                            arg(arg='spreadsheet_key', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='groupbys', annotation=None, type_comment=None),
                            arg(arg='view_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_access_token',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='scope',
                                        value=Constant(value='https://spreadsheets.google.com/feeds', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fields', ctx=Store())],
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
                                    attr='fields_view_get',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='view_id',
                                        value=Name(id='view_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='view_type',
                                        value=Constant(value='tree', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='doc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='XML',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='fields', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='arch', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='display_fields', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='node', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='doc', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//field', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='modifiers', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='modifiers', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='loads',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='node', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='modifiers', kind=None)],
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
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='modifiers', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='invisible', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='modifiers', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='column_invisible', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='display_fields', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='node', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='name', kind=None)],
                                                                keywords=[],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='display_fields', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='domain', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value="'", kind=None),
                                                            Constant(value="\\'", kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='"', kind=None),
                                                    Constant(value="'", kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='True', kind=None),
                                            Constant(value='true', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='False', kind=None),
                                    Constant(value='false', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='groupbys', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='groupbys', ctx=Load()),
                                                Name(id='fields', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='formula', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='=oe_read_group("%s";"%s";"%s";"%s")', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='model', ctx=Load()),
                                                Name(id='fields', ctx=Load()),
                                                Name(id='groupbys', ctx=Load()),
                                                Name(id='domain', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='formula', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='=oe_browse("%s";"%s";"%s")', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='model', ctx=Load()),
                                                Name(id='fields', ctx=Load()),
                                                Name(id='domain', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dbname', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_cr',
                                    ctx=Load(),
                                ),
                                attr='dbname',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Subscript(
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
                                                    slice=Constant(value='res.users', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='browse',
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
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='read',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Constant(value='login', kind=None),
                                                Constant(value='password', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='username', ctx=Store())],
                            value=Subscript(
                                value=Name(id='user', ctx=Load()),
                                slice=Constant(value='login', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='password', ctx=Store())],
                            value=Subscript(
                                value=Name(id='user', ctx=Load()),
                                slice=Constant(value='password', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='password', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='config_formula', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='=oe_settings("%s";"%s")', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='url', ctx=Load()),
                                                Name(id='dbname', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='config_formula', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='=oe_settings("%s";"%s";"%s";"%s")', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='url', ctx=Load()),
                                                Name(id='dbname', ctx=Load()),
                                                Name(id='username', ctx=Load()),
                                                Name(id='password', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='request', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='<feed xmlns="http://www.w3.org/2005/Atom"\n      xmlns:batch="http://schemas.google.com/gdata/batch"\n      xmlns:gs="http://schemas.google.com/spreadsheets/2006">\n  <id>https://spreadsheets.google.com/feeds/cells/{key}/od6/private/full</id>\n  <entry>\n    <batch:id>A1</batch:id>\n    <batch:operation type="update"/>\n    <id>https://spreadsheets.google.com/feeds/cells/{key}/od6/private/full/R1C1</id>\n    <link rel="edit" type="application/atom+xml"\n      href="https://spreadsheets.google.com/feeds/cells/{key}/od6/private/full/R1C1"/>\n    <gs:cell row="1" col="1" inputValue="{formula}"/>\n  </entry>\n  <entry>\n    <batch:id>A2</batch:id>\n    <batch:operation type="update"/>\n    <id>https://spreadsheets.google.com/feeds/cells/{key}/od6/private/full/R60C15</id>\n    <link rel="edit" type="application/atom+xml"\n      href="https://spreadsheets.google.com/feeds/cells/{key}/od6/private/full/R60C15"/>\n    <gs:cell row="60" col="15" inputValue="{config}"/>\n  </entry>\n</feed>', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Name(id='spreadsheet_key', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='formula',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='misc', ctx=Load()),
                                                attr='html_escape',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='formula', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='config',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='misc', ctx=Load()),
                                                attr='html_escape',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='config_formula', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='req', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='post',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='https://spreadsheets.google.com/feeds/cells/%s/od6/private/full/batch?%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='spreadsheet_key', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='werkzeug', ctx=Load()),
                                                                    attr='urls',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='url_encode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Dict(
                                                                    keys=[
                                                                        Constant(value='v', kind=None),
                                                                        Constant(value='access_token', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value=3, kind=None),
                                                                        Name(id='access_token', ctx=Load()),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='data',
                                                value=Name(id='request', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='headers',
                                                value=Dict(
                                                    keys=[
                                                        Constant(value='content-type', kind=None),
                                                        Constant(value='If-Match', kind=None),
                                                    ],
                                                    values=[
                                                        Constant(value='application/atom+xml', kind=None),
                                                        Constant(value='*', kind=None),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='TIMEOUT', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='An error occured while writing the formula on the Google Spreadsheet.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='description', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='\n        formula: %s\n        ', kind=None),
                                op=Mod(),
                                right=Name(id='formula', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='attachment_id', ctx=Load()),
                            body=[
                                Expr(
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
                                                        slice=Constant(value='ir.attachment', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='attachment_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='description', kind=None)],
                                                values=[Name(id='description', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
                    name='set_spreadsheet',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='groupbys', annotation=None, type_comment=None),
                            arg(arg='view_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='config', ctx=Store())],
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
                                args=[Constant(value='google_spreadsheet.google_spreadsheet_template', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='title', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Spreadsheet %s', kind=None),
                                op=Mod(),
                                right=Name(id='model', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='copy_doc',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Name(id='config', ctx=Load()),
                                        attr='google_drive_resource_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='title', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(key=|/d/)([A-Za-z0-9-_]+)', kind=None),
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='url', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mo', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='key', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mo', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write_config_formula',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='id', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='key', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                    Name(id='domain', ctx=Load()),
                                    Name(id='groupbys', ctx=Load()),
                                    Name(id='view_id', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
    ],
    type_ignores=[],
)
