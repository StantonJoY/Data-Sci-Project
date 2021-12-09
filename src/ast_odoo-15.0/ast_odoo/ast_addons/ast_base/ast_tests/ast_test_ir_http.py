Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Assign(
            targets=[Name(id='GIF', ctx=Store())],
            value=Constant(value=b'R0lGODdhAQABAIAAAP///////ywAAAAAAQABAAACAkQBADs=', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='test_ir_http_mimetype',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_ir_http_mimetype_attachment',
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
                            value=Constant(value=' Test mimetype for attachment ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='datas', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Name(id='GIF', ctx=Load()),
                                            Constant(value='file.gif', kind=None),
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
                                        Name(id='status', ctx=Store()),
                                        Name(id='headers', ctx=Store()),
                                        Name(id='content', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='id',
                                        value=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='mimetype',
                                        value=Constant(value=None, kind=None),
                                    ),
                                    keyword(
                                        arg='default_mimetype',
                                        value=Constant(value='application/octet-stream', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='headers', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Content-Type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='image/gif', kind=None),
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
                    name='test_ir_http_mimetype_attachment_name',
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
                            value=Constant(value=' Test mimetype for attachment with bad name', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='datas', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Name(id='GIF', ctx=Load()),
                                            Constant(value='file.png', kind=None),
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
                                        Name(id='status', ctx=Store()),
                                        Name(id='headers', ctx=Store()),
                                        Name(id='content', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='id',
                                        value=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='mimetype',
                                        value=Constant(value=None, kind=None),
                                    ),
                                    keyword(
                                        arg='default_mimetype',
                                        value=Constant(value='application/octet-stream', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='headers', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Content-Type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='image/png', kind=None),
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
                    name='test_ir_http_mimetype_basic_field',
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
                            value=Constant(value=' Test mimetype for classic field ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='image_1920', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Name(id='GIF', ctx=Load()),
                                            Constant(value='Test mimetype basic field', kind=None),
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
                                        Name(id='status', ctx=Store()),
                                        Name(id='headers', ctx=Store()),
                                        Name(id='content', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='res.partner', kind=None),
                                    ),
                                    keyword(
                                        arg='id',
                                        value=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Constant(value='image_1920', kind=None),
                                    ),
                                    keyword(
                                        arg='default_mimetype',
                                        value=Constant(value='application/octet-stream', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='headers', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Content-Type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='image/gif', kind=None),
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
                    name='test_ir_http_mimetype_computed_field',
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
                            value=Constant(value=' Test mimetype for computed field wich resize picture', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='prop', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.property', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='fields_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='value_binary', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.model.fields', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='search',
                                                        ctx=Load(),
                                                    ),
                                                    args=[List(elts=[], ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg='limit',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Property binary', kind=None),
                                            Name(id='GIF', ctx=Load()),
                                            Constant(value='binary', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='resized', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='image_process',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='prop', ctx=Load()),
                                        attr='value_binary',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='size',
                                        value=Tuple(
                                            elts=[
                                                Constant(value=64, kind=None),
                                                Constant(value=64, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='prop', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value_binary', kind=None)],
                                        values=[Name(id='resized', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='status', ctx=Store()),
                                        Name(id='headers', ctx=Store()),
                                        Name(id='content', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='ir.property', kind=None),
                                    ),
                                    keyword(
                                        arg='id',
                                        value=Attribute(
                                            value=Name(id='prop', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Constant(value='value_binary', kind=None),
                                    ),
                                    keyword(
                                        arg='default_mimetype',
                                        value=Constant(value='application/octet-stream', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='headers', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Content-Type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='image/gif', kind=None),
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
                    name='test_ir_http_attachment_access',
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
                            value=Constant(value=' Test attachment access with and without access token ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='public_user', ctx=Store())],
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
                                args=[Constant(value='base.public_user', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='datas', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Name(id='GIF', ctx=Load()),
                                            Constant(value='image.gif', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='defaults', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='default_mimetype', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='attachment', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='image/gif', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='test_access',
                            args=arguments(
                                posonlyargs=[],
                                args=[],
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
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='invalidate_cache',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='status', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
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
                                                        slice=Constant(value='ir.http', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='public_user', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='binary_content',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Call(
                                                    func=Name(id='dict', ctx=Load()),
                                                    args=[Name(id='defaults', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg=None,
                                                            value=Name(id='kwargs', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='status', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Name(id='test_access', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Constant(value=403, kind=None),
                                    Constant(value='no access', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Name(id='test_access', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='access_token',
                                        value=Constant(value='Secret', kind='u'),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Constant(value=403, kind=None),
                                    Constant(value='no access if access token for attachment without access token', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='access_token',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Secret', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Name(id='test_access', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='access_token',
                                        value=Constant(value='Secret', kind='u'),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Constant(value=200, kind=None),
                                    Constant(value='access for correct access token', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Name(id='test_access', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='access_token',
                                        value=Constant(value='Wrong', kind='u'),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Constant(value=403, kind=None),
                                    Constant(value='no access for wrong access token', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='public',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Name(id='test_access', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Constant(value=200, kind=None),
                                    Constant(value='access for attachment with access', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Name(id='test_access', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='access_token',
                                        value=Constant(value='Wrong', kind='u'),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Constant(value=403, kind=None),
                                    Constant(value='no access for wrong access token for attachment with access', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Name(id='test_access', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Constant(value=404, kind=None),
                                    Constant(value='no access for deleted attachment', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Call(
                                func=Name(id='test_access', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='access_token',
                                        value=Constant(value='Secret', kind='u'),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Constant(value=404, kind=None),
                                    Constant(value='no access with access token for deleted attachment', kind=None),
                                ],
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
    ],
    type_ignores=[],
)
