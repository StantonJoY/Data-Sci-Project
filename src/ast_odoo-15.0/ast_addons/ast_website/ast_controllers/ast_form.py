Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='IntegrityError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='BadRequest', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='plaintext2html', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='ValidationError', asname=None),
                alias(name='UserError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_qweb_fields',
            names=[alias(name='nl2br', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteForm',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='website_form_empty',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value='', kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/website/form/', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='multilang',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='website_form',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='csrf_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='params',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='csrf_token', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='validate_csrf',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='csrf_token', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BadRequest', ctx=Load()),
                                        args=[Constant(value='Session expired (invalid CSRF token)', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='savepoint',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        If(
                                            test=Call(
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
                                                    attr='_verify_request_recaptcha_token',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='website_form', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_handle_website_form',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='model_name', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg=None,
                                                                value=Name(id='kwargs', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='error', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Suspicious activity detected by Google reCaptcha.', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='ValidationError', ctx=Load()),
                                            Name(id='UserError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Assign(
                                            targets=[Name(id='error', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='args',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Name(id='error', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/website/form/<string:model_name>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_website_form',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='model_record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.model', kind=None),
                                                ctx=Load(),
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
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='model_name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_form_access', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='model_record', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='error', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="The form's specified model does not exist", kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
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
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='extract_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='model_record', ctx=Load()),
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='params',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValidationError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='dumps',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='error_fields', kind=None)],
                                                        values=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='e', ctx=Load()),
                                                                    attr='args',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
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
                            finalbody=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='id_record', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='insert_record',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='request', ctx=Load()),
                                            Name(id='model_record', ctx=Load()),
                                            Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='record', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='custom', kind=None),
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='meta', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='id_record', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='insert_attachment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='model_record', ctx=Load()),
                                                    Name(id='id_record', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='attachments', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='model_name', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='mail.mail', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='request', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Name(id='model_name', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='sudo',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='browse',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='id_record', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='send',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IntegrityError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='dumps',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=False, kind=None)],
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
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='form_builder_model_model', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='model_record', ctx=Load()),
                                attr='model',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='form_builder_model', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='model_record', ctx=Load()),
                                attr='name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='form_builder_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='id_record', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='id', kind=None)],
                                        values=[Name(id='id_record', ctx=Load())],
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
                Assign(
                    targets=[Name(id='_meta_label', ctx=Store())],
                    value=BinOp(
                        left=Constant(value='%s\n________\n\n', kind=None),
                        op=Mod(),
                        right=Call(
                            func=Name(id='_', ctx=Load()),
                            args=[Constant(value='Metadata', kind=None)],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='identity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_label', annotation=None, type_comment=None),
                            arg(arg='field_input', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Name(id='field_input', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='integer',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_label', annotation=None, type_comment=None),
                            arg(arg='field_input', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[Name(id='field_input', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='floating',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_label', annotation=None, type_comment=None),
                            arg(arg='field_input', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='float', ctx=Load()),
                                args=[Name(id='field_input', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_label', annotation=None, type_comment=None),
                            arg(arg='field_input', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='plaintext2html', ctx=Load()),
                                args=[Name(id='field_input', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='boolean',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_label', annotation=None, type_comment=None),
                            arg(arg='field_input', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[Name(id='field_input', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='binary',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_label', annotation=None, type_comment=None),
                            arg(arg='field_input', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64encode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='field_input', ctx=Load()),
                                            attr='read',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='one2many',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_label', annotation=None, type_comment=None),
                            arg(arg='field_input', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[Name(id='i', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='i', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='field_input', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=',', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
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
                    name='many2many',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_label', annotation=None, type_comment=None),
                            arg(arg='field_input', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=List(
                                elts=[
                                    BinOp(
                                        left=IfExp(
                                            test=Name(id='args', ctx=Load()),
                                            body=Subscript(
                                                value=Name(id='args', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            orelse=Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='one2many',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='field_label', ctx=Load()),
                                                        Name(id='field_input', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
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
                    targets=[Name(id='_input_filters', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='char', kind=None),
                            Constant(value='text', kind=None),
                            Constant(value='html', kind=None),
                            Constant(value='date', kind=None),
                            Constant(value='datetime', kind=None),
                            Constant(value='many2one', kind=None),
                            Constant(value='one2many', kind=None),
                            Constant(value='many2many', kind=None),
                            Constant(value='selection', kind=None),
                            Constant(value='boolean', kind=None),
                            Constant(value='integer', kind=None),
                            Constant(value='float', kind=None),
                            Constant(value='binary', kind=None),
                            Constant(value='monetary', kind=None),
                        ],
                        values=[
                            Name(id='identity', ctx=Load()),
                            Name(id='identity', ctx=Load()),
                            Name(id='html', ctx=Load()),
                            Name(id='identity', ctx=Load()),
                            Name(id='identity', ctx=Load()),
                            Name(id='integer', ctx=Load()),
                            Name(id='one2many', ctx=Load()),
                            Name(id='many2many', ctx=Load()),
                            Name(id='identity', ctx=Load()),
                            Name(id='boolean', ctx=Load()),
                            Name(id='integer', ctx=Load()),
                            Name(id='floating', ctx=Load()),
                            Name(id='binary', ctx=Load()),
                            Name(id='floating', ctx=Load()),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='extract_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='dest_model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='model',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='record', kind=None),
                                    Constant(value='attachments', kind=None),
                                    Constant(value='custom', kind=None),
                                    Constant(value='meta', kind=None),
                                ],
                                values=[
                                    Dict(keys=[], values=[]),
                                    List(elts=[], ctx=Load()),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='authorized_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_form_writable_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='error_fields', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='custom_fields', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='field_name', ctx=Store()),
                                    Name(id='field_value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='field_value', ctx=Load()),
                                            Constant(value='filename', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='field_name', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='field_name', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='[', kind=None),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='field_name', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='authorized_fields', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='authorized_fields', ctx=Load()),
                                                                slice=Name(id='field_name', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='binary', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=Constant(value='record', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='field_name', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='field_value', ctx=Load()),
                                                                    attr='read',
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='field_value', ctx=Load()),
                                                                attr='stream',
                                                                ctx=Load(),
                                                            ),
                                                            attr='seek',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=0, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='authorized_fields', ctx=Load()),
                                                                    slice=Name(id='field_name', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='manual', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=BinOp(
                                                                    left=Name(id='field_name', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value='_filename', kind=None),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='dest_model', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='data', ctx=Load()),
                                                                        slice=Constant(value='record', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=BinOp(
                                                                        left=Name(id='field_name', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value='_filename', kind=None),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Attribute(
                                                                value=Name(id='field_value', ctx=Load()),
                                                                attr='filename',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='field_value', ctx=Load()),
                                                            attr='field_name',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='field_name', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='data', ctx=Load()),
                                                                slice=Constant(value='attachments', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='field_value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='field_name', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='authorized_fields', ctx=Load())],
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='input_filter', ctx=Store())],
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_input_filters',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='authorized_fields', ctx=Load()),
                                                                        slice=Name(id='field_name', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='data', ctx=Load()),
                                                                        slice=Constant(value='record', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(id='field_name', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Name(id='input_filter', ctx=Load()),
                                                                args=[
                                                                    Name(id='self', ctx=Load()),
                                                                    Name(id='field_name', ctx=Load()),
                                                                    Name(id='field_value', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='ValueError', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='error_fields', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='field_name', ctx=Load())],
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
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='field_name', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='context', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='custom_fields', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='field_name', ctx=Load()),
                                                                            Name(id='field_value', ctx=Load()),
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
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='custom', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='\n', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=BinOp(
                                            left=Constant(value='%s : %s', kind='u'),
                                            op=Mod(),
                                            right=Name(id='v', ctx=Load()),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='v', ctx=Store()),
                                                iter=Name(id='custom_fields', ctx=Load()),
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
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
                                args=[Constant(value='website_form_enable_metadata', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='environ', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='headers',
                                            ctx=Load(),
                                        ),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='meta', kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='%s : %s\n%s : %s\n%s : %s\n%s : %s\n', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Constant(value='IP', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='environ', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='REMOTE_ADDR', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='USER_AGENT', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='environ', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='HTTP_USER_AGENT', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='ACCEPT_LANGUAGE', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='environ', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='HTTP_ACCEPT_LANGUAGE', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='REFERER', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='environ', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='HTTP_REFERER', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='dest_model', ctx=Load()),
                                    Constant(value='website_form_input_filter', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='record', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dest_model', ctx=Load()),
                                            attr='website_form_input_filter',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='request', ctx=Load()),
                                            Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='record', kind=None),
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
                            targets=[Name(id='missing_required_fields', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='label', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='label', ctx=Store()),
                                                Name(id='field', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='authorized_fields', ctx=Load()),
                                                attr='items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='field', ctx=Load()),
                                                        slice=Constant(value='required', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Compare(
                                                            left=Name(id='label', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                Subscript(
                                                                    value=Name(id='data', ctx=Load()),
                                                                    slice=Constant(value='record', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
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
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[Name(id='error_fields', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='error_fields', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='missing_required_fields', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
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
                    name='insert_record',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='request', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='custom', annotation=None, type_comment=None),
                            arg(arg='meta', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='model_name', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='model',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='model_name', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='mail.mail', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='reply_to', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='email_from', kind=None)],
                                                        keywords=[],
                                                    ),
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='model_name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mail_create_nosubscribe',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='custom', ctx=Load()),
                                    Name(id='meta', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='_custom_label', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s\n___________\n\n', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Other Information:', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='model_name', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='mail.mail', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='_custom_label', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s\n___________\n\n', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='This message has been posted on your website!', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='default_field', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='website_form_default_field_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='default_field_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='default_field', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='custom_content', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=IfExp(
                                                test=Name(id='default_field_data', ctx=Load()),
                                                body=BinOp(
                                                    left=Name(id='default_field_data', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value='\n\n', kind=None),
                                                ),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                            op=Add(),
                                            right=IfExp(
                                                test=Name(id='custom', ctx=Load()),
                                                body=BinOp(
                                                    left=BinOp(
                                                        left=Name(id='_custom_label', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='custom', ctx=Load()),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value='\n\n', kind=None),
                                                ),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                        ),
                                        op=Add(),
                                        right=IfExp(
                                            test=Name(id='meta', ctx=Load()),
                                            body=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_meta_label',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Name(id='meta', ctx=Load()),
                                            ),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='default_field', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='default_field', ctx=Load()),
                                                            attr='ttype',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='html', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='model_name', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='mail.mail', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='custom_content', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='nl2br', ctx=Load()),
                                                        args=[Name(id='custom_content', ctx=Load())],
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
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Attribute(
                                                                value=Name(id='default_field', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        values=[Name(id='custom_content', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='body', kind=None),
                                                    Constant(value='model', kind=None),
                                                    Constant(value='message_type', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='nl2br', ctx=Load()),
                                                        args=[Name(id='custom_content', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Name(id='model_name', ctx=Load()),
                                                    Constant(value='comment', kind=None),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='mail_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='mail.message', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
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
                            value=Attribute(
                                value=Name(id='record', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='insert_attachment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='id_record', annotation=None, type_comment=None),
                            arg(arg='files', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='orphan_attachment_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_name', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='model',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='id_record', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='authorized_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_form_writable_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='file', ctx=Store()),
                            iter=Name(id='files', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='custom_field', ctx=Store())],
                                    value=Compare(
                                        left=Attribute(
                                            value=Name(id='file', ctx=Load()),
                                            attr='field_name',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='authorized_fields', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attachment_value', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='datas', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='file', ctx=Load()),
                                                attr='filename',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='encodebytes',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='file', ctx=Load()),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='model_name', ctx=Load()),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attachment_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.attachment', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='attachment_value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='attachment_id', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='custom_field', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    slice=Attribute(
                                                        value=Name(id='file', ctx=Load()),
                                                        attr='field_name',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='attachment_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='orphan_attachment_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment_id', ctx=Load()),
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
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='model_name', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='mail.mail', kind=None)],
                            ),
                            body=[
                                If(
                                    test=Name(id='orphan_attachment_ids', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='body', kind=None),
                                                    Constant(value='model', kind=None),
                                                    Constant(value='message_type', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='attachment_ids', kind=None),
                                                    Constant(value='subtype_id', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='<p>Attached files : </p>', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(id='model_name', ctx=Load()),
                                                    Constant(value='comment', kind=None),
                                                    Name(id='id_record', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Name(id='orphan_attachment_ids', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.model.data', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_xmlid_to_res_id',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='mail.mt_comment', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='mail_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='mail.message', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                For(
                                    target=Name(id='attachment_id_id', ctx=Store()),
                                    iter=Name(id='orphan_attachment_ids', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='attachment_ids',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Name(id='attachment_id_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
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
