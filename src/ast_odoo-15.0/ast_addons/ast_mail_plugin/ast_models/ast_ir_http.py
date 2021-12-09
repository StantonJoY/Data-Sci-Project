Module(
    body=[
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='BadRequest', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            name='IrHttp',
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
                    value=Constant(value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_auth_method_outlook',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Authorization', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='access_token', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BadRequest', ctx=Load()),
                                        args=[Constant(value='Access token missing', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='access_token', ctx=Load()),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Bearer ', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='access_token', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='access_token', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=7, kind=None),
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
                            targets=[Name(id='user_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.users.apikeys', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_check_credentials',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='scope',
                                        value=Constant(value='odoo.plugin.outlook', kind=None),
                                    ),
                                    keyword(
                                        arg='key',
                                        value=Name(id='access_token', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='user_id', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BadRequest', ctx=Load()),
                                        args=[Constant(value='Access token invalid', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='uid',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='user_id', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
