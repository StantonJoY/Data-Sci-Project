Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='mimetypes', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.utils', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='tools', asname=None),
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
            module='odoo.tools.mimetypes',
            names=[alias(name='guess_mimetype', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.urls',
            names=[alias(name='url_encode', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='logger', ctx=Store())],
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
            name='Web_Unsplash',
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
                    name='_get_access_key',
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='_has_unsplash_key_rights',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Return(
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
                                        args=[Constant(value='unsplash.access_key', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Raise(
                            exc=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='exceptions',
                                        ctx=Load(),
                                    ),
                                    attr='NotFound',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    name='_notify_download',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Notifies Unsplash from an image download. (API requirement)\n            :param url: the download_url of the image to be notified\n\n            This method won't return anything. This endpoint should just be\n            pinged with a simple GET request for Unsplash to increment the image\n            view counter.\n        ", kind=None),
                        ),
                        Try(
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='url', ctx=Load()),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='https://api.unsplash.com/photos/', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='registry',
                                                            ctx=Load(),
                                                        ),
                                                        attr='in_test_mode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='ERROR: Unknown Unsplash notify URL!', kind=None)],
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
                                    targets=[Name(id='access_key', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_access_key',
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
                                            value=Name(id='requests', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='url', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='params',
                                                value=Call(
                                                    func=Name(id='url_encode', ctx=Load()),
                                                    args=[
                                                        Dict(
                                                            keys=[Constant(value='client_id', kind=None)],
                                                            values=[Name(id='access_key', ctx=Load())],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
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
                                                    value=Name(id='logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Unsplash download notification failed: ', kind=None),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='e', ctx=Load())],
                                                            keywords=[],
                                                        ),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_unsplash_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='unsplashurls', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n            unsplashurls = {\n                image_id1: {\n                    url: image_url,\n                    download_url: download_url,\n                },\n                image_id2: {\n                    url: image_url,\n                    download_url: download_url,\n                },\n                .....\n            }\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='slugify',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='s', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Keeps only alphanumeric characters, hyphens and spaces from a string.\n                The string will also be truncated to 1024 characters max.\n                :param s: the string to be filtered\n                :return: the sanitized string\n            ', kind=None),
                                ),
                                Return(
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Constant(value='', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                ListComp(
                                                    elt=Name(id='c', ctx=Load()),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='c', ctx=Store()),
                                                            iter=Name(id='s', ctx=Load()),
                                                            ifs=[
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='c', ctx=Load()),
                                                                                attr='isalnum',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        Compare(
                                                                            left=Name(id='c', ctx=Load()),
                                                                            ops=[In()],
                                                                            comparators=[
                                                                                Call(
                                                                                    func=Name(id='list', ctx=Load()),
                                                                                    args=[Constant(value='- ', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=1024, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='unsplashurls', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='uploads', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Attachments', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.attachment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='query', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Name(id='slugify', ctx=Load()),
                                args=[Name(id='query', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res_model', kind=None),
                                    Constant(value='ir.ui.view', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='res_model', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='ir.ui.view', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res_id', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='kwargs', ctx=Load()),
                                                slice=Constant(value='res_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='res_id', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='unsplashurls', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='value', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='url', kind=None)],
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
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='url', ctx=Load()),
                                                                attr='startswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='https://images.unsplash.com/', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='request', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='registry',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='in_test_mode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='ERROR: Unknown Unsplash URL!: ', kind=None),
                                                                op=Add(),
                                                                right=Name(id='url', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='Exception', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='ERROR: Unknown Unsplash URL!', kind=None)],
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
                                            targets=[Name(id='req', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='url', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='req', ctx=Load()),
                                                    attr='status_code',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='requests', ctx=Load()),
                                                            attr='codes',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ok',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='image_base64', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64encode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='req', ctx=Load()),
                                                        attr='content',
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
                                            type=Attribute(
                                                value=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='ConnectionError',
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Connection Error: ', kind=None),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='e', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='Timeout',
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Timeout: ', kind=None),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='e', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[Name(id='image_base64', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_process',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='image_base64', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='verify_resolution',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mimetype', ctx=Store())],
                                    value=Call(
                                        func=Name(id='guess_mimetype', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='image_base64', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='query', ctx=Store()),
                                    op=Add(),
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='mimetypes', ctx=Load()),
                                                    attr='guess_extension',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='mimetype', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='url_frags', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='unsplash', kind=None),
                                            Name(id='key', ctx=Load()),
                                            Name(id='query', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Attachments', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='url', kind=None),
                                                    Constant(value='mimetype', kind=None),
                                                    Constant(value='datas', kind=None),
                                                    Constant(value='public', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='description', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Constant(value='_', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='url_frags', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='/', kind=None),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Constant(value='/', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='url_frags', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Name(id='mimetype', ctx=Load()),
                                                    Name(id='image_base64', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='res_model', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='ir.ui.view', kind=None)],
                                                    ),
                                                    Name(id='res_id', ctx=Load()),
                                                    Name(id='res_model', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='value', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='description', kind=None)],
                                                        keywords=[],
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
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='generate_access_token',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='uploads', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='_get_media_info',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_notify_download',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='value', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='download_url', kind=None)],
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
                        Return(
                            value=Name(id='uploads', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_unsplash/attachment/add', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fetch_unsplash_images',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='access_key', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_key',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='app_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_unsplash_app_id',
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
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='access_key', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='app_id', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[Constant(value='key_not_found', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='post', ctx=Load()),
                                    slice=Constant(value='client_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='access_key', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='https://api.unsplash.com/search/photos/', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Call(
                                            func=Name(id='url_encode', ctx=Load()),
                                            args=[Name(id='post', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='status_code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='codes',
                                            ctx=Load(),
                                        ),
                                        attr='ok',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='status_code',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_unsplash/fetch_images', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_unsplash_app_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Return(
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
                                args=[Constant(value='unsplash.app_id', kind=None)],
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
                            args=[Constant(value='/web_unsplash/get_app_id', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_unsplash',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='_has_unsplash_key_rights',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
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
                                                        slice=Constant(value='ir.config_parameter', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='set_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='unsplash.app_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='post', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='appId', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
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
                                                        slice=Constant(value='ir.config_parameter', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='set_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='unsplash.access_key', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='post', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='key', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Raise(
                            exc=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='exceptions',
                                        ctx=Load(),
                                    ),
                                    attr='NotFound',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web_unsplash/save_unsplash', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
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
