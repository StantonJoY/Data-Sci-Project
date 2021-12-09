Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='threading',
            names=[alias(name='Thread', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.main',
            names=[
                alias(name='drivers', asname=None),
                alias(name='interfaces', asname=None),
                alias(name='iot_devices', asname=None),
            ],
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
            name='InterfaceMetaClass',
            bases=[Name(id='type', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__new__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='clsname', annotation=None, type_comment=None),
                            arg(arg='bases', annotation=None, type_comment=None),
                            arg(arg='attrs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='new_interface', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='InterfaceMetaClass', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__new__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Name(id='clsname', ctx=Load()),
                                    Name(id='bases', ctx=Load()),
                                    Name(id='attrs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='interfaces', ctx=Load()),
                                    slice=Name(id='clsname', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='new_interface', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='new_interface', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Interface',
            bases=[Name(id='Thread', ctx=Load())],
            keywords=[
                keyword(
                    arg='metaclass',
                    value=Name(id='InterfaceMetaClass', ctx=Load()),
                ),
            ],
            body=[
                Assign(
                    targets=[Name(id='_loop_delay', ctx=Store())],
                    value=Constant(value=3, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_detected_devices', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='connection_type', ctx=Store())],
                    value=Constant(value='', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Interface', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='drivers',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Name(id='d', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='d', ctx=Store()),
                                                iter=Name(id='drivers', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='d', ctx=Load()),
                                                            attr='connection_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='connection_type',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='d', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Attribute(
                                                value=Name(id='d', ctx=Load()),
                                                attr='priority',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='reverse',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='run',
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
                        While(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='connection_type',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='drivers',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='update_iot_devices',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_devices',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_loop_delay',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='sleep',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_loop_delay',
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
                FunctionDef(
                    name='update_iot_devices',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='devices', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Dict(keys=[], values=[])],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='added', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='devices', ctx=Load()),
                                        attr='keys',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_detected_devices',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='removed', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_detected_devices',
                                    ctx=Load(),
                                ),
                                op=Sub(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='devices', ctx=Load()),
                                        attr='keys',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_detected_devices',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='devices', ctx=Load()),
                                    attr='keys',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='identifier', ctx=Store()),
                            iter=Name(id='removed', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='identifier', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='iot_devices', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='iot_devices', ctx=Load()),
                                                        slice=Name(id='identifier', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='disconnect',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Device %s is now disconnected', kind=None),
                                                    Name(id='identifier', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='identifier', ctx=Store()),
                            iter=Name(id='added', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='driver', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='drivers',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='driver', ctx=Load()),
                                                    attr='supported',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='devices', ctx=Load()),
                                                        slice=Name(id='identifier', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Device %s is now connected', kind=None),
                                                            Name(id='identifier', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='d', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='driver', ctx=Load()),
                                                        args=[
                                                            Name(id='identifier', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='devices', ctx=Load()),
                                                                slice=Name(id='identifier', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='d', ctx=Load()),
                                                            attr='daemon',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='iot_devices', ctx=Load()),
                                                            slice=Name(id='identifier', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='d', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='d', ctx=Load()),
                                                            attr='start',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Break(),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
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
                FunctionDef(
                    name='get_devices',
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
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
