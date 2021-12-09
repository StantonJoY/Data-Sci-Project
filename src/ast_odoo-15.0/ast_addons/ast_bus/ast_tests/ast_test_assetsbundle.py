Module(
    body=[
        Import(
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ClassDef(
            name='BusWebTests',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_bundle_sends_bus',
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
                            value=Constant(value="\n        Tests two things:\n        - Messages are posted to the bus when assets change\n          i.e. their hash has been recomputed and differ from the attachment's\n        - The interface deals with those bus messages by displaying one notification\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='db_name', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                attr='db_name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bundle_xml_ids', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='web.assets_common', kind=None),
                                    Constant(value='web.assets_backend', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='bundle', ctx=Store()),
                            iter=Name(id='bundle_xml_ids', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='OR',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    BinOp(
                                                                        left=Name(id='bundle', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value='%', kind=None),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='_clear_cache',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sendones', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='patched_sendone',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='self', annotation=None, type_comment=None),
                                    arg(arg='channel', annotation=None, type_comment=None),
                                    arg(arg='notificationType', annotation=None, type_comment=None),
                                    arg(arg='message', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Control API and number of messages posted to the bus linked to\n            bundle_changed events ', kind=None),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='notificationType', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='bundle_changed', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sendones', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='channel', ctx=Load()),
                                                            Name(id='message', ctx=Load()),
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
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='bus.bus', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='_sendone', kind=None),
                                    Name(id='patched_sendone', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='admin', kind=None),
                                    Constant(value='admin', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url_open',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='sendones', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
                                    BinOp(
                                        left=Constant(value='Received %s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Constant(value='\n', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                GeneratorExp(
                                                    elt=BinOp(
                                                        left=Constant(value='%s - %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Subscript(
                                                                    value=Name(id='tmp', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='tmp', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='tmp', ctx=Store()),
                                                            iter=Name(id='sendones', ctx=Load()),
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
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='channel', ctx=Store()),
                                    Name(id='message', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='sendones', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='channel', ctx=Load()),
                                            Constant(value='broadcast', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='message', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='message', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='name', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='bundle_xml_ids', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='message', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(id='str', ctx=Load()),
                                                ],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                        Constant(value='assets_bundle', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
