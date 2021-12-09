Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='serial', asname=None)],
        ),
        Import(
            names=[alias(name='socket', asname=None)],
        ),
        Import(
            names=[alias(name='usb.core', asname=None)],
        ),
        Import(
            names=[alias(name='usb.util', asname=None)],
        ),
        ImportFrom(
            module='escpos',
            names=[alias(name='*', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='constants',
            names=[alias(name='*', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='exceptions',
            names=[alias(name='*', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='time',
            names=[alias(name='sleep', asname=None)],
            level=0,
        ),
        ClassDef(
            name='Usb',
            bases=[Name(id='Escpos', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Define USB printer ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='idVendor', annotation=None, type_comment=None),
                            arg(arg='idProduct', annotation=None, type_comment=None),
                            arg(arg='interface', annotation=None, type_comment=None),
                            arg(arg='in_ep', annotation=None, type_comment=None),
                            arg(arg='out_ep', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        @param idVendor  : Vendor ID\n        @param idProduct : Product ID\n        @param interface : USB device interface\n        @param in_ep     : Input end point\n        @param out_ep    : Output end point\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='errorText',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value='ERROR PRINTER\n\n\n\n\n\n', kind=None),
                                op=Add(),
                                right=Name(id='PAPER_FULL_CUT', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='idVendor',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='idVendor', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='idProduct',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='idProduct', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='interface',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='interface', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='in_ep',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='in_ep', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='out_ep',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='out_ep', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='usb', ctx=Load()),
                                            attr='version_info',
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='usb', ctx=Load()),
                                                    attr='version_info',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='usb', ctx=Load()),
                                                        attr='version_info',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='a1', kind=None),
                                                            Constant(value='a2', kind=None),
                                                            Constant(value='a3', kind=None),
                                                            Constant(value='b1', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write_kwargs',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='interface',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='interface',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write_kwargs',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open',
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
                            value=Constant(value=' Search device on USB tree and set is as escpos device ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='usb', ctx=Load()),
                                        attr='core',
                                        ctx=Load(),
                                    ),
                                    attr='find',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='idVendor',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='idVendor',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='idProduct',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='idProduct',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='NoDeviceError', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device',
                                                ctx=Load(),
                                            ),
                                            attr='is_kernel_driver_active',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='interface',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='device',
                                                        ctx=Load(),
                                                    ),
                                                    attr='detach_kernel_driver',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='interface',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device',
                                                ctx=Load(),
                                            ),
                                            attr='set_configuration',
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
                                                value=Name(id='usb', ctx=Load()),
                                                attr='util',
                                                ctx=Load(),
                                            ),
                                            attr='claim_interface',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='interface',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='cfg', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device',
                                                ctx=Load(),
                                            ),
                                            attr='get_active_configuration',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='intf', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='cfg', ctx=Load()),
                                        slice=Tuple(
                                            elts=[
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='in_ep',
                                            ctx=Load(),
                                        ),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='is_IN', ctx=Store())],
                                                    value=Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='e', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='usb', ctx=Load()),
                                                                        attr='util',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='endpoint_direction',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='e', ctx=Load()),
                                                                        attr='bEndpointAddress',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='usb', ctx=Load()),
                                                                        attr='util',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='ENDPOINT_IN',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='is_OUT', ctx=Store())],
                                                    value=Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='e', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='usb', ctx=Load()),
                                                                        attr='util',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='endpoint_direction',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='e', ctx=Load()),
                                                                        attr='bEndpointAddress',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='usb', ctx=Load()),
                                                                        attr='util',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='ENDPOINT_OUT',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='endpoint_in', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='usb', ctx=Load()),
                                                                attr='util',
                                                                ctx=Load(),
                                                            ),
                                                            attr='find_descriptor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='intf', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='custom_match',
                                                                value=Name(id='is_IN', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='endpoint_out', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='usb', ctx=Load()),
                                                                attr='util',
                                                                ctx=Load(),
                                                            ),
                                                            attr='find_descriptor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='intf', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='custom_match',
                                                                value=Name(id='is_OUT', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='in_ep',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='endpoint_in', ctx=Load()),
                                                        attr='bEndpointAddress',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='out_ep',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='endpoint_out', ctx=Load()),
                                                        attr='bEndpointAddress',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='usb', ctx=Load()),
                                                            attr='core',
                                                            ctx=Load(),
                                                        ),
                                                        attr='USBError',
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='in_ep',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=130, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='out_ep',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=1, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='usb', ctx=Load()),
                                            attr='core',
                                            ctx=Load(),
                                        ),
                                        attr='USBError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='HandleDeviceError', ctx=Load()),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='close',
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
                            targets=[Name(id='i', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        While(
                            test=Constant(value=True, kind=None),
                            body=[
                                Try(
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='device',
                                                            ctx=Load(),
                                                        ),
                                                        attr='is_kernel_driver_active',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='interface',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='usb', ctx=Load()),
                                                                attr='util',
                                                                ctx=Load(),
                                                            ),
                                                            attr='release_interface',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='device',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='interface',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='device',
                                                                ctx=Load(),
                                                            ),
                                                            attr='attach_kernel_driver',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='interface',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='usb', ctx=Load()),
                                                                attr='util',
                                                                ctx=Load(),
                                                            ),
                                                            attr='dispose_resources',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='device',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='device',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Attribute(
                                                    value=Name(id='usb', ctx=Load()),
                                                    attr='core',
                                                    ctx=Load(),
                                                ),
                                                attr='USBError',
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                AugAssign(
                                                    target=Name(id='i', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='i', ctx=Load()),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=10, kind=None)],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Constant(value=False, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='sleep', ctx=Load()),
                                        args=[Constant(value=0.1, kind=None)],
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
                    name='_raw',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='msg', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Print any command sent in raw format ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='msg', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='out_ep',
                                                ctx=Load(),
                                            ),
                                            Name(id='msg', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='timeout',
                                                value=Constant(value=5000, kind=None),
                                            ),
                                            keyword(
                                                arg=None,
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='write_kwargs',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='out_ep',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='errorText',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='write_kwargs',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='TicketNotPrinted', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
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
                    name='__extract_status',
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
                            targets=[Name(id='maxiterate', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rep', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Name(id='rep', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='maxiterate', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='maxiterate', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=10000, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='NoStatusError', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='r', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='device',
                                                        ctx=Load(),
                                                    ),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='in_ep',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=20, kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='interface',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='tolist',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                While(
                                    test=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='r', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='rep', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='r', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='rep', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_printer_status',
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
                            targets=[Name(id='status', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='printer', kind=None),
                                    Constant(value='offline', kind=None),
                                    Constant(value='error', kind=None),
                                    Constant(value='paper', kind=None),
                                ],
                                values=[
                                    Dict(keys=[], values=[]),
                                    Dict(keys=[], values=[]),
                                    Dict(keys=[], values=[]),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='out_ep',
                                        ctx=Load(),
                                    ),
                                    Name(id='DLE_EOT_PRINTER', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write_kwargs',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='printer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='__extract_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='out_ep',
                                        ctx=Load(),
                                    ),
                                    Name(id='DLE_EOT_OFFLINE', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write_kwargs',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='offline', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='__extract_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='out_ep',
                                        ctx=Load(),
                                    ),
                                    Name(id='DLE_EOT_ERROR', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write_kwargs',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='error', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='__extract_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='out_ep',
                                        ctx=Load(),
                                    ),
                                    Name(id='DLE_EOT_PAPER', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='write_kwargs',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='paper', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='__extract_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='printer', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='status_code', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='printer', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='printer', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='status_error', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=BinOp(
                                        left=Name(id='printer', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=147, kind=None),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value=18, kind=None)],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='printer', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='online', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='bool', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=Name(id='printer', ctx=Load()),
                                            op=BitAnd(),
                                            right=Constant(value=8, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='printer', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='recovery', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='printer', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=32, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='printer', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='paper_feed_on', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='printer', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=64, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='printer', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='drawer_pin_high', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='printer', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=4, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='offline', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='status_code', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='offline', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='offline', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='status_error', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=BinOp(
                                        left=Name(id='offline', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=147, kind=None),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value=18, kind=None)],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='offline', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='cover_open', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='offline', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=4, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='offline', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='paper_feed_on', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='offline', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=8, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='offline', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='paper', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='bool', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=Name(id='offline', ctx=Load()),
                                            op=BitAnd(),
                                            right=Constant(value=32, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='offline', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='error', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='offline', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=64, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='error', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='status_code', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='error', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='error', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='status_error', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=BinOp(
                                        left=Name(id='error', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=147, kind=None),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value=18, kind=None)],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='error', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='recoverable', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='error', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=4, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='error', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='autocutter', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='error', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=8, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='error', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='unrecoverable', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='error', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=32, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='error', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='auto_recoverable', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='bool', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=Name(id='error', ctx=Load()),
                                            op=BitAnd(),
                                            right=Constant(value=64, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='paper', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='status_code', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='paper', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='paper', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='status_error', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=BinOp(
                                        left=Name(id='paper', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=147, kind=None),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value=18, kind=None)],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='paper', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='near_end', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='paper', ctx=Load()),
                                        op=BitAnd(),
                                        right=Constant(value=12, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='paper', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='present', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='bool', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=Name(id='paper', ctx=Load()),
                                            op=BitAnd(),
                                            right=Constant(value=96, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
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
                FunctionDef(
                    name='__del__',
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
                            value=Constant(value=' Release USB interface ', kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='device',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='close',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
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
            name='Serial',
            bases=[Name(id='Escpos', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Define Serial printer ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='devfile', annotation=None, type_comment=None),
                            arg(arg='baudrate', annotation=None, type_comment=None),
                            arg(arg='bytesize', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='/dev/ttyS0', kind=None),
                            Constant(value=9600, kind=None),
                            Constant(value=8, kind=None),
                            Constant(value=1, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        @param devfile  : Device file under dev filesystem\n        @param baudrate : Baud rate for serial transmission\n        @param bytesize : Serial buffer size\n        @param timeout  : Read/Write timeout\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='devfile',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='devfile', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='baudrate',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='baudrate', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='bytesize',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='bytesize', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='timeout',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='timeout', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open',
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
                            value=Constant(value=' Setup serial port and set is as escpos device ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='serial', ctx=Load()),
                                    attr='Serial',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='port',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='devfile',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='baudrate',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='baudrate',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='bytesize',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='bytesize',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='parity',
                                        value=Attribute(
                                            value=Name(id='serial', ctx=Load()),
                                            attr='PARITY_NONE',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='stopbits',
                                        value=Attribute(
                                            value=Name(id='serial', ctx=Load()),
                                            attr='STOPBITS_ONE',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='timeout',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='dsrdtr',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[Constant(value='Serial printer enabled', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Unable to open serial printer on: %s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='devfile',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_raw',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='msg', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Print any command sent in raw format ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='msg', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__del__',
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
                            value=Constant(value=' Close Serial interface ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device',
                                                ctx=Load(),
                                            ),
                                            attr='close',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Network',
            bases=[Name(id='Escpos', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Define Network printer ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='host', annotation=None, type_comment=None),
                            arg(arg='port', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=9100, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        @param host : Printer's hostname or IP address\n        @param port : Port to write to\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='host',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='host', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='port',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='port', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open',
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
                            value=Constant(value=' Open TCP socket and set it as escpos device ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='socket', ctx=Load()),
                                    attr='socket',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='socket', ctx=Load()),
                                        attr='AF_INET',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='socket', ctx=Load()),
                                        attr='SOCK_STREAM',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device',
                                        ctx=Load(),
                                    ),
                                    attr='connect',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='host',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='port',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Could not open socket for %s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='host',
                                                    ctx=Load(),
                                                ),
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
                    name='_raw',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='msg', annotation=None, type_comment=None),
                        ],
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device',
                                        ctx=Load(),
                                    ),
                                    attr='send',
                                    ctx=Load(),
                                ),
                                args=[Name(id='msg', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__del__',
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
                            value=Constant(value=' Close TCP connection ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device',
                                        ctx=Load(),
                                    ),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[],
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
