Module(
    body=[
        ImportFrom(
            module='re',
            names=[
                alias(name='sub', asname=None),
                alias(name='finditer', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.interface',
            names=[alias(name='Interface', asname=None)],
            level=0,
        ),
        ClassDef(
            name='DisplayInterface',
            bases=[Name(id='Interface', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_loop_delay', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='connection_type', ctx=Store())],
                    value=Constant(value='display', kind=None),
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
                        Assign(
                            targets=[Name(id='display_devices', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='displays', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='check_output',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='tvservice', kind=None),
                                                    Constant(value='-l', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='x_screen', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='match', ctx=Store()),
                            iter=Call(
                                func=Name(id='finditer', ctx=Load()),
                                args=[
                                    Constant(value='Display Number (\\d), type HDMI (\\d)', kind=None),
                                    Name(id='displays', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='display_id', ctx=Store()),
                                                Name(id='hdmi_id', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='groups',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tvservice_output', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subprocess', ctx=Load()),
                                                            attr='check_output',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='tvservice', kind=None),
                                                                    Constant(value='-nv', kind=None),
                                                                    Name(id='display_id', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='tvservice_output', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='display_name', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='tvservice_output', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='=', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='display_identifier', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='sub', ctx=Load()),
                                                                args=[
                                                                    Constant(value='[^a-zA-Z0-9 ]+', kind=None),
                                                                    Constant(value='', kind=None),
                                                                    Name(id='display_name', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=' ', kind=None),
                                                            Constant(value='_', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value='_', kind=None),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Name(id='hdmi_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='iot_device', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='identifier', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='x_screen', kind=None),
                                                ],
                                                values=[
                                                    Name(id='display_identifier', ctx=Load()),
                                                    Name(id='display_name', ctx=Load()),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='x_screen', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='display_devices', ctx=Load()),
                                                    slice=Name(id='display_identifier', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='iot_device', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='x_screen', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='display_devices', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='display_devices', ctx=Load()),
                                            slice=Constant(value='distant_display', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Distant Display', kind=None)],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='display_devices', ctx=Load()),
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
