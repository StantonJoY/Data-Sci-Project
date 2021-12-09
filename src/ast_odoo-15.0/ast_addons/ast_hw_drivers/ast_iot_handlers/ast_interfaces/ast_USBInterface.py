Module(
    body=[
        ImportFrom(
            module='usb',
            names=[alias(name='core', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.interface',
            names=[alias(name='Interface', asname=None)],
            level=0,
        ),
        ClassDef(
            name='USBInterface',
            bases=[Name(id='Interface', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='connection_type', ctx=Store())],
                    value=Constant(value='usb', kind=None),
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
                        Expr(
                            value=Constant(value="\n        USB devices are identified by a combination of their `idVendor` and\n        `idProduct`. We can't be sure this combination in unique per equipment.\n        To still allow connecting multiple similar equipments, we complete the\n        identifier by a counter. The drawbacks are we can't be sure the equipments\n        will get the same identifiers after a reboot or a disconnect/reconnect.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='usb_devices', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='devs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='core', ctx=Load()),
                                    attr='find',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='find_all',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cpt', ctx=Store())],
                            value=Constant(value=2, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='dev', ctx=Store()),
                            iter=Name(id='devs', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='identifier', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='usb_%04x:%04x', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='dev', ctx=Load()),
                                                    attr='idVendor',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='dev', ctx=Load()),
                                                    attr='idProduct',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='identifier', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='usb_devices', ctx=Load())],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='identifier', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value='_%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='cpt', ctx=Load()),
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='cpt', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='usb_devices', ctx=Load()),
                                            slice=Name(id='identifier', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='dev', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='usb_devices', ctx=Load()),
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
