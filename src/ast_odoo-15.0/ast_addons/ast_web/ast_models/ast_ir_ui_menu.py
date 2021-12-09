Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='IrUiMenu',
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
                    value=Constant(value='ir.ui.menu', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='load_web_menus',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='debug', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Loads all menu items (all applications and their sub-menus) and\n        processes them to be used by the webclient. Mainly, it associates with\n        each application (top level menu) the action of its first child menu\n        that is associated with an action (recursively), i.e. with the action\n        to execute when the opening the app.\n\n        :return: the menus (including the images in Base64)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='menus', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='load_menus',
                                    ctx=Load(),
                                ),
                                args=[Name(id='debug', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='web_menus', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='menu', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='menus', ctx=Load()),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='menu', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='web_menus', ctx=Load()),
                                                    slice=Constant(value='root', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='children', kind=None),
                                                    Constant(value='appID', kind=None),
                                                    Constant(value='xmlid', kind=None),
                                                    Constant(value='actionID', kind=None),
                                                    Constant(value='actionModel', kind=None),
                                                    Constant(value='webIcon', kind=None),
                                                    Constant(value='webIconData', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='root', kind=None),
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='children', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='action', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='menu', ctx=Load()),
                                                slice=Constant(value='action', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='menu', ctx=Load()),
                                                    slice=Constant(value='id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='app_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='child', ctx=Store())],
                                                    value=Name(id='menu', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                While(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='child', ctx=Load()),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='action', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='action', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='child', ctx=Load()),
                                                                slice=Constant(value='action', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='child', ctx=Store())],
                                                            value=IfExp(
                                                                test=Subscript(
                                                                    value=Name(id='child', ctx=Load()),
                                                                    slice=Constant(value='children', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                body=Subscript(
                                                                    value=Name(id='menus', ctx=Load()),
                                                                    slice=Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='child', ctx=Load()),
                                                                            slice=Constant(value='children', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                orelse=Constant(value=False, kind=None),
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
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='action_model', ctx=Store()),
                                                        Name(id='action_id', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Name(id='action', ctx=Load()),
                                                body=Call(
                                                    func=Attribute(
                                                        value=Name(id='action', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=',', kind=None)],
                                                    keywords=[],
                                                ),
                                                orelse=Tuple(
                                                    elts=[
                                                        Constant(value=False, kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='action_id', ctx=Store())],
                                            value=IfExp(
                                                test=Name(id='action_id', ctx=Load()),
                                                body=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='action_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                orelse=Constant(value=False, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='web_menus', ctx=Load()),
                                                    slice=Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='children', kind=None),
                                                    Constant(value='appID', kind=None),
                                                    Constant(value='xmlid', kind=None),
                                                    Constant(value='actionID', kind=None),
                                                    Constant(value='actionModel', kind=None),
                                                    Constant(value='webIcon', kind=None),
                                                    Constant(value='webIconData', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='children', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='app_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='xmlid', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='action_id', ctx=Load()),
                                                    Name(id='action_model', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='web_icon', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='menu', ctx=Load()),
                                                        slice=Constant(value='web_icon_data', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='web_menus', ctx=Load()),
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
