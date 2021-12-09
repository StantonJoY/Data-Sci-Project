Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.bus.controllers.main',
            names=[alias(name='BusController', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessDenied', asname=None)],
            level=0,
        ),
        ClassDef(
            name='EditorCollaborationController',
            bases=[Name(id='BusController', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_poll',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='dbname', annotation=None, type_comment=None),
                            arg(arg='channels', annotation=None, type_comment=None),
                            arg(arg='last', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='uid',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='channels', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='channels', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='channel', ctx=Store()),
                                    iter=Name(id='channels', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='channel', ctx=Load()),
                                                    Name(id='str', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='match', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='re', ctx=Load()),
                                                            attr='match',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='editor_collaboration:(\\w+(?:.\\w+)*):(\\w+):([\\d]+)', kind=None),
                                                            Name(id='channel', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='match', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='model_name', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='match', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='field_name', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='match', ctx=Load()),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='res_id', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='match', ctx=Load()),
                                                                        slice=Constant(value=3, kind=None),
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
                                                                operand=Call(
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
                                                                        attr='has_group',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='base.group_user', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            body=[
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Name(id='AccessDenied', ctx=Load()),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    cause=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='document', ctx=Store())],
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
                                                                    attr='browse',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[Name(id='res_id', ctx=Load())],
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
                                                                    value=Name(id='document', ctx=Load()),
                                                                    attr='check_access_rights',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='read', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='document', ctx=Load()),
                                                                    attr='check_field_access_rights',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='read', kind=None),
                                                                    List(
                                                                        elts=[Name(id='field_name', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='document', ctx=Load()),
                                                                    attr='check_access_rule',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='read', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='document', ctx=Load()),
                                                                    attr='check_access_rights',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='write', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='document', ctx=Load()),
                                                                    attr='check_field_access_rights',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='write', kind=None),
                                                                    List(
                                                                        elts=[Name(id='field_name', ctx=Load())],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='document', ctx=Load()),
                                                                    attr='check_access_rule',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='write', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='channels', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='request', ctx=Load()),
                                                                                attr='db',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='editor_collaboration', kind=None),
                                                                            Name(id='model_name', ctx=Load()),
                                                                            Name(id='field_name', ctx=Load()),
                                                                            Name(id='res_id', ctx=Load()),
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
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='EditorCollaborationController', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_poll',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='dbname', ctx=Load()),
                                    Name(id='channels', ctx=Load()),
                                    Name(id='last', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
