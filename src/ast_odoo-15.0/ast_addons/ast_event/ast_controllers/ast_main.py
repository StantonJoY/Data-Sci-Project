Module(
    body=[
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='NotFound', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='Controller', asname=None),
                alias(name='request', asname=None),
                alias(name='route', asname=None),
                alias(name='content_disposition', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='EventController',
            bases=[Name(id='Controller', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='event_ics_file',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='files', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event', ctx=Load()),
                                    attr='_get_ics_file',
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
                                operand=Compare(
                                    left=Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    ops=[In()],
                                    comparators=[Name(id='files', ctx=Load())],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='NotFound', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Subscript(
                                value=Name(id='files', ctx=Load()),
                                slice=Attribute(
                                    value=Name(id='event', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='content', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='Content-Type', kind=None),
                                                    Constant(value='application/octet-stream', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='Content-Length', kind=None),
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='content', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='Content-Disposition', kind=None),
                                                    Call(
                                                        func=Name(id='content_disposition', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='%s.ics', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='event', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
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
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[
                                List(
                                    elts=[Constant(value='/event/<model("event.event"):event>/ics', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
