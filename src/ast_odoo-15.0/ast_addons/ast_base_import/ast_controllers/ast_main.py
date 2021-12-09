Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='misc', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ImportController',
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
                    name='set_file',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='file', annotation=None, type_comment=None),
                            arg(arg='import_id', annotation=None, type_comment=None),
                            arg(arg='jsonp', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='callback', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='import_id', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[Name(id='import_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='written', ctx=Store())],
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
                                                slice=Constant(value='base_import.import', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='import_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='file', kind=None),
                                            Constant(value='file_name', kind=None),
                                            Constant(value='file_type', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='file', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='file', ctx=Load()),
                                                attr='filename',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='file', ctx=Load()),
                                                attr='content_type',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='window.top.%s(%s)', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='misc', ctx=Load()),
                                                attr='html_escape',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='jsonp', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='dumps',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Dict(
                                                    keys=[Constant(value='result', kind=None)],
                                                    values=[Name(id='written', ctx=Load())],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
                            args=[Constant(value='/base_import/set_file', kind=None)],
                            keywords=[
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
