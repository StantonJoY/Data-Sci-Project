Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='math', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='os.path', asname=None)],
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='netifaces', asname='ni')],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        Try(
            body=[
                ImportFrom(
                    module='escpos',
                    names=[alias(name='*', asname=None)],
                    level=2,
                ),
                ImportFrom(
                    module='escpos.exceptions',
                    names=[alias(name='*', asname=None)],
                    level=2,
                ),
                ImportFrom(
                    module='escpos.printer',
                    names=[alias(name='Usb', asname=None)],
                    level=2,
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[
                                Name(id='escpos', ctx=Store()),
                                Name(id='printer', ctx=Store()),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        ImportFrom(
            module='queue',
            names=[alias(name='Queue', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='threading',
            names=[
                alias(name='Thread', asname=None),
                alias(name='Lock', asname=None),
            ],
            level=0,
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='usb.core', asname=None)],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='usb', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.controllers',
            names=[alias(name='proxy', asname=None)],
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
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='datetime', ctx=Load()),
                    attr='strptime',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='2012-01-01', kind=None),
                    Constant(value='%Y-%m-%d', kind=None),
                ],
                keywords=[],
            ),
        ),
        ClassDef(
            name='EscposDriver',
            bases=[Name(id='Thread', ctx=Load())],
            keywords=[],
            body=[
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
                                    value=Name(id='Thread', ctx=Load()),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='queue',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='Queue', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='lock',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='Lock', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='status',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='status', kind=None),
                                    Constant(value='messages', kind=None),
                                ],
                                values=[
                                    Constant(value='connecting', kind=None),
                                    List(elts=[], ctx=Load()),
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
                    name='connected_usb_devices',
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
                            targets=[Name(id='connected', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        ClassDef(
                            name='FindUsbClass',
                            bases=[Name(id='object', ctx=Load())],
                            keywords=[],
                            body=[
                                FunctionDef(
                                    name='__init__',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[
                                            arg(arg='self', annotation=None, type_comment=None),
                                            arg(arg='usb_class', annotation=None, type_comment=None),
                                        ],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_class',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='usb_class', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                                FunctionDef(
                                    name='__call__',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[
                                            arg(arg='self', annotation=None, type_comment=None),
                                            arg(arg='device', annotation=None, type_comment=None),
                                        ],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='device', ctx=Load()),
                                                    attr='bDeviceClass',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_class',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='cfg', ctx=Store()),
                                            iter=Name(id='device', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='intf', ctx=Store())],
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
                                                        args=[Name(id='cfg', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='bInterfaceClass',
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_class',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='intf', ctx=Load()),
                                                        ops=[IsNot()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Constant(value=True, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                        ),
                        Assign(
                            targets=[Name(id='printers', ctx=Store())],
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
                                        arg='find_all',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='custom_match',
                                        value=Call(
                                            func=Name(id='FindUsbClass', ctx=Load()),
                                            args=[Constant(value=7, kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='printers', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='printers', ctx=Store())],
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
                                                arg='find_all',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='idVendor',
                                                value=Constant(value=1208, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='printers', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='printers', ctx=Store())],
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
                                                arg='find_all',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='idVendor',
                                                value=Constant(value=1305, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='printer', ctx=Store()),
                            iter=Name(id='printers', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='description', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='usb', ctx=Load()),
                                                                attr='util',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='printer', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='printer', ctx=Load()),
                                                                attr='iManufacturer',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value=' ', kind=None),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='usb', ctx=Load()),
                                                            attr='util',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get_string',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='printer', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='printer', ctx=Load()),
                                                            attr='iProduct',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Can not get printer description: %s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='e', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='description', ctx=Store())],
                                                    value=Constant(value='Unknown printer', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='connected', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='vendor', kind=None),
                                                    Constant(value='product', kind=None),
                                                    Constant(value='name', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='printer', ctx=Load()),
                                                        attr='idVendor',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='printer', ctx=Load()),
                                                        attr='idProduct',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='description', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='connected', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='lockedstart',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='lock',
                                        ctx=Load(),
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='is_alive',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='daemon',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='start',
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_escpos_printer',
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
                            targets=[Name(id='printers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='connected_usb_devices',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='printers', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='print_dev', ctx=Store())],
                                            value=Call(
                                                func=Name(id='Usb', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='printers', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='vendor', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='printers', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='product', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='HandleDeviceError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Return(
                                                    value=Constant(value=None, kind=None),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='set_status',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='connected', kind=None),
                                            BinOp(
                                                left=Constant(value='Connected to %s (in=0x%02x,out=0x%02x)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='printers', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='print_dev', ctx=Load()),
                                                            attr='in_ep',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='print_dev', ctx=Load()),
                                                            attr='out_ep',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='print_dev', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='set_status',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='disconnected', kind=None),
                                            Constant(value='Printer Not Found', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_status',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='push_task',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='status', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='status',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_cashbox',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='printer', annotation=None, type_comment=None),
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
                                    value=Name(id='printer', ctx=Load()),
                                    attr='cashdraw',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=2, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='printer', ctx=Load()),
                                    attr='cashdraw',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=5, kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='set_status',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
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
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='status', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=' : ', kind=None),
                                        ),
                                        op=Add(),
                                        right=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='message', ctx=Load()),
                                                Constant(value='no message', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='status', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='status',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='status', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='message', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='status',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='messages', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='message', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='status',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='messages', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=1, kind=None),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='status',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='messages', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='message', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='status',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='status', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='status', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='message', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='status',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='messages', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[Name(id='message', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='status',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='messages', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='status', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='error', kind=None)],
                                    ),
                                    Name(id='message', ctx=Load()),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='ESC/POS Error: %s', kind=None),
                                            Name(id='message', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='status', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='disconnected', kind=None)],
                                            ),
                                            Name(id='message', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='ESC/POS Device Disconnected: %s', kind=None),
                                                    Name(id='message', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
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
                        Assign(
                            targets=[Name(id='printer', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='escpos', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ESC/POS cannot initialize, please verify system dependencies.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Return(value=None),
                            ],
                            orelse=[],
                        ),
                        While(
                            test=Constant(value=True, kind=None),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='error', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='timestamp', ctx=Store()),
                                                        Name(id='task', ctx=Store()),
                                                        Name(id='data', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='queue',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=True, kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='printer', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_escpos_printer',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='printer', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='task', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='status', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='queue',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='put',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='timestamp', ctx=Load()),
                                                                            Name(id='task', ctx=Load()),
                                                                            Name(id='data', ctx=Load()),
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
                                                Assign(
                                                    targets=[Name(id='error', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='sleep',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=5, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='task', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='receipt', kind=None)],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='timestamp', ctx=Load()),
                                                                ops=[GtE()],
                                                                comparators=[
                                                                    BinOp(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='time', ctx=Load()),
                                                                                attr='time',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Sub(),
                                                                        right=BinOp(
                                                                            left=BinOp(
                                                                                left=Constant(value=1, kind=None),
                                                                                op=Mult(),
                                                                                right=Constant(value=60, kind=None),
                                                                            ),
                                                                            op=Mult(),
                                                                            right=Constant(value=60, kind=None),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='print_receipt_body',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='printer', ctx=Load()),
                                                                            Name(id='data', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='printer', ctx=Load()),
                                                                            attr='cut',
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
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='task', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='xml_receipt', kind=None)],
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='timestamp', ctx=Load()),
                                                                        ops=[GtE()],
                                                                        comparators=[
                                                                            BinOp(
                                                                                left=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='time', ctx=Load()),
                                                                                        attr='time',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Sub(),
                                                                                right=BinOp(
                                                                                    left=BinOp(
                                                                                        left=Constant(value=1, kind=None),
                                                                                        op=Mult(),
                                                                                        right=Constant(value=60, kind=None),
                                                                                    ),
                                                                                    op=Mult(),
                                                                                    right=Constant(value=60, kind=None),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='printer', ctx=Load()),
                                                                                    attr='receipt',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='data', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='task', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='cashbox', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='timestamp', ctx=Load()),
                                                                                ops=[GtE()],
                                                                                comparators=[
                                                                                    BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='time', ctx=Load()),
                                                                                                attr='time',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Sub(),
                                                                                        right=Constant(value=12, kind=None),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='open_cashbox',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='printer', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='task', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='status', kind=None)],
                                                                            ),
                                                                            body=[Pass()],
                                                                            orelse=[],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='error', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='NoDeviceError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='print', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='No device found %s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='e', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='HandleDeviceError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Assign(
                                                    targets=[Name(id='printer', ctx=Store())],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='print', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Impossible to handle the device due to previous error %s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='e', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='TicketNotPrinted', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='print', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='The ticket does not seems to have been fully printed %s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='e', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='NoStatusError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='print', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Impossible to get the status of the printer %s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='e', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='set_status',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='error', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[
                                        If(
                                            test=Name(id='error', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='queue',
                                                                ctx=Load(),
                                                            ),
                                                            attr='put',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='timestamp', ctx=Load()),
                                                                    Name(id='task', ctx=Load()),
                                                                    Name(id='data', ctx=Load()),
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
                                        If(
                                            test=Name(id='printer', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='printer', ctx=Load()),
                                                            attr='close',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='printer', ctx=Store())],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
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
                    name='push_task',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='task', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='lockedstart',
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='queue',
                                        ctx=Load(),
                                    ),
                                    attr='put',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='time',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='task', ctx=Load()),
                                            Name(id='data', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='print_receipt_body',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='eprint', annotation=None, type_comment=None),
                            arg(arg='receipt', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='check',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='string', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='string', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=True, kind=None)],
                                            ),
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[Name(id='string', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='string', ctx=Load()),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='price',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='amount', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Constant(value='{0:.', kind=None),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='receipt', ctx=Load()),
                                                                    slice=Constant(value='precision', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='price', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='f}', kind=None),
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='amount', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='money',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='amount', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Constant(value='{0:.', kind=None),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='receipt', ctx=Load()),
                                                                    slice=Constant(value='precision', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='money', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='f}', kind=None),
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='amount', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='quantity',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='amount', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='math', ctx=Load()),
                                                attr='floor',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='amount', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='amount', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value='{0:.', kind=None),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='receipt', ctx=Load()),
                                                                            slice=Constant(value='precision', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='quantity', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='f}', kind=None),
                                                    ),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='amount', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='amount', ctx=Load())],
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
                            name='printline',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='left', annotation=None, type_comment=None),
                                    arg(arg='right', annotation=None, type_comment=None),
                                    arg(arg='width', annotation=None, type_comment=None),
                                    arg(arg='ratio', annotation=None, type_comment=None),
                                    arg(arg='indent', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value='', kind=None),
                                    Constant(value=40, kind=None),
                                    Constant(value=0.5, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lwidth', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='width', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='ratio', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='rwidth', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='width', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='lwidth', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='lwidth', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='lwidth', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='indent', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='left', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='left', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Name(id='lwidth', ctx=Load()),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='left', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='lwidth', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='left', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='left', ctx=Load()),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Constant(value=' ', kind=None),
                                                    op=Mult(),
                                                    right=BinOp(
                                                        left=Name(id='lwidth', ctx=Load()),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='left', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='right', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='right', ctx=Load()),
                                        slice=Slice(
                                            lower=UnaryOp(
                                                op=USub(),
                                                operand=Name(id='rwidth', ctx=Load()),
                                            ),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='right', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='rwidth', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='right', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Constant(value=' ', kind=None),
                                                    op=Mult(),
                                                    right=BinOp(
                                                        left=Name(id='rwidth', ctx=Load()),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='right', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Name(id='right', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=Constant(value=' ', kind=None),
                                                    op=Mult(),
                                                    right=Name(id='indent', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='left', ctx=Load()),
                                            ),
                                            op=Add(),
                                            right=Name(id='right', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Constant(value='\n', kind=None),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='print_taxes',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Assign(
                                    targets=[Name(id='taxes', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='receipt', ctx=Load()),
                                        slice=Constant(value='tax_details', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='tax', ctx=Store()),
                                    iter=Name(id='taxes', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='eprint', ctx=Load()),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='printline', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='tax', ctx=Load()),
                                                                    slice=Constant(value='tax', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='price', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='tax', ctx=Load()),
                                                                        slice=Constant(value='amount', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='width',
                                                                value=Constant(value=40, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='ratio',
                                                                value=Constant(value=0.6, kind=None),
                                                            ),
                                                        ],
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
                        If(
                            test=Subscript(
                                value=Subscript(
                                    value=Name(id='receipt', ctx=Load()),
                                    slice=Constant(value='company', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='logo', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='align',
                                                value=Constant(value='center', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='print_base64_image',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='receipt', ctx=Load()),
                                                    slice=Constant(value='company', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='logo', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='\n', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='align',
                                                value=Constant(value='center', kind=None),
                                            ),
                                            keyword(
                                                arg='type',
                                                value=Constant(value='b', kind=None),
                                            ),
                                            keyword(
                                                arg='height',
                                                value=Constant(value=2, kind=None),
                                            ),
                                            keyword(
                                                arg='width',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='receipt', ctx=Load()),
                                                        slice=Constant(value='company', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='align',
                                        value=Constant(value='center', kind=None),
                                    ),
                                    keyword(
                                        arg='type',
                                        value=Constant(value='b', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='receipt', ctx=Load()),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='contact_address', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='receipt', ctx=Load()),
                                                        slice=Constant(value='company', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='contact_address', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='receipt', ctx=Load()),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='phone', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value='Tel:', kind=None),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='receipt', ctx=Load()),
                                                            slice=Constant(value='company', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='phone', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='receipt', ctx=Load()),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='vat', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value='VAT:', kind=None),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='receipt', ctx=Load()),
                                                            slice=Constant(value='company', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='vat', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='receipt', ctx=Load()),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='email', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='receipt', ctx=Load()),
                                                        slice=Constant(value='company', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='email', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='receipt', ctx=Load()),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='receipt', ctx=Load()),
                                                        slice=Constant(value='company', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='website', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='receipt', ctx=Load()),
                                        slice=Constant(value='header', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='receipt', ctx=Load()),
                                                    slice=Constant(value='header', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='receipt', ctx=Load()),
                                        slice=Constant(value='cashier', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value='-', kind=None),
                                                    op=Mult(),
                                                    right=Constant(value=32, kind=None),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value='Served by ', kind=None),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Name(id='receipt', ctx=Load()),
                                                        slice=Constant(value='cashier', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
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
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n\n', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='align',
                                        value=Constant(value='center', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='receipt', ctx=Load()),
                                slice=Constant(value='orderlines', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pricestr', ctx=Store())],
                                    value=Call(
                                        func=Name(id='price', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Constant(value='price_display', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=Constant(value='discount', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=Constant(value='unit_name', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='Units', kind=None)],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=Constant(value='quantity', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='eprint', ctx=Load()),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='printline', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='line', ctx=Load()),
                                                                slice=Constant(value='product_name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='pricestr', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='ratio',
                                                                value=Constant(value=0.6, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='eprint', ctx=Load()),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='printline', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='line', ctx=Load()),
                                                                slice=Constant(value='product_name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='ratio',
                                                                value=Constant(value=0.6, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=Constant(value='discount', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='eprint', ctx=Load()),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='printline', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=BinOp(
                                                                            left=Constant(value='Discount: ', kind=None),
                                                                            op=Add(),
                                                                            right=Call(
                                                                                func=Name(id='str', ctx=Load()),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='line', ctx=Load()),
                                                                                        slice=Constant(value='discount', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value='%', kind=None),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='ratio',
                                                                        value=Constant(value=0.6, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='indent',
                                                                        value=Constant(value=2, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=Constant(value='unit_name', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='Units', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='eprint', ctx=Load()),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='printline', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=BinOp(
                                                                            left=Call(
                                                                                func=Name(id='quantity', ctx=Load()),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='line', ctx=Load()),
                                                                                        slice=Constant(value='quantity', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            op=Add(),
                                                                            right=Constant(value=' x ', kind=None),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='price', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    slice=Constant(value='price', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    Name(id='pricestr', ctx=Load()),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='ratio',
                                                                        value=Constant(value=0.6, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='indent',
                                                                        value=Constant(value=2, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='eprint', ctx=Load()),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='printline', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=BinOp(
                                                                            left=BinOp(
                                                                                left=Call(
                                                                                    func=Name(id='quantity', ctx=Load()),
                                                                                    args=[
                                                                                        Subscript(
                                                                                            value=Name(id='line', ctx=Load()),
                                                                                            slice=Constant(value='quantity', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Add(),
                                                                                right=Subscript(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    slice=Constant(value='unit_name', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            op=Add(),
                                                                            right=Constant(value=' x ', kind=None),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='price', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    slice=Constant(value='price', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    Name(id='pricestr', ctx=Load()),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='ratio',
                                                                        value=Constant(value=0.6, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='indent',
                                                                        value=Constant(value=2, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='taxincluded', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='money', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='receipt', ctx=Load()),
                                            slice=Constant(value='subtotal', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Name(id='money', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='receipt', ctx=Load()),
                                                slice=Constant(value='total_with_tax', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='printline', ctx=Load()),
                                                args=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='-------', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='printline', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Subtotal', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='money', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='receipt', ctx=Load()),
                                                                slice=Constant(value='subtotal', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='width',
                                                        value=Constant(value=40, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='ratio',
                                                        value=Constant(value=0.6, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='print_taxes', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='taxincluded', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='printline', ctx=Load()),
                                        args=[
                                            Constant(value='', kind=None),
                                            Constant(value='-------', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='align',
                                        value=Constant(value='center', kind=None),
                                    ),
                                    keyword(
                                        arg='height',
                                        value=Constant(value=2, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='printline', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='         TOTAL', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='money', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='receipt', ctx=Load()),
                                                        slice=Constant(value='total_with_tax', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='width',
                                                value=Constant(value=40, kind=None),
                                            ),
                                            keyword(
                                                arg='ratio',
                                                value=Constant(value=0.6, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n\n', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='align',
                                        value=Constant(value='center', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='receipt', ctx=Load()),
                                slice=Constant(value='paymentlines', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='printline', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Constant(value='journal', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='money', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='line', ctx=Load()),
                                                                slice=Constant(value='amount', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='ratio',
                                                        value=Constant(value=0.6, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='align',
                                        value=Constant(value='center', kind=None),
                                    ),
                                    keyword(
                                        arg='height',
                                        value=Constant(value=2, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='printline', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='        CHANGE', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='money', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='receipt', ctx=Load()),
                                                        slice=Constant(value='change', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='width',
                                                value=Constant(value=40, kind=None),
                                            ),
                                            keyword(
                                                arg='ratio',
                                                value=Constant(value=0.6, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='align',
                                        value=Constant(value='center', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n', kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='receipt', ctx=Load()),
                                    slice=Constant(value='total_discount', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='printline', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Discounts', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='money', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='receipt', ctx=Load()),
                                                                slice=Constant(value='total_discount', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='width',
                                                        value=Constant(value=40, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='ratio',
                                                        value=Constant(value=0.6, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='taxincluded', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='print_taxes', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='receipt', ctx=Load()),
                                        slice=Constant(value='footer', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='eprint', ctx=Load()),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value='\n', kind=None),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Name(id='receipt', ctx=Load()),
                                                        slice=Constant(value='footer', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n\n', kind=None),
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
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Subscript(
                                            value=Name(id='receipt', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Constant(value='\n', kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='eprint', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=Call(
                                                                        func=Attribute(
                                                                            value=Call(
                                                                                func=Name(id='str', ctx=Load()),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Subscript(
                                                                                            value=Name(id='receipt', ctx=Load()),
                                                                                            slice=Constant(value='date', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='date', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='zfill',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value=2, kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value='/', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Attribute(
                                                                        value=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[
                                                                                BinOp(
                                                                                    left=Subscript(
                                                                                        value=Subscript(
                                                                                            value=Name(id='receipt', ctx=Load()),
                                                                                            slice=Constant(value='date', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='month', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    op=Add(),
                                                                                    right=Constant(value=1, kind=None),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='zfill',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value=2, kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value='/', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Subscript(
                                                                                value=Name(id='receipt', ctx=Load()),
                                                                                slice=Constant(value='date', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='year', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='zfill',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=4, kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value=' ', kind=None),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='receipt', ctx=Load()),
                                                                        slice=Constant(value='date', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='hour', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='zfill',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=2, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            op=Add(),
                                            right=Constant(value=':', kind=None),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='receipt', ctx=Load()),
                                                                slice=Constant(value='date', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='minute', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='zfill',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=2, kind=None)],
                                            keywords=[],
                                        ),
                                    ),
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
        Assign(
            targets=[Name(id='driver', ctx=Store())],
            value=Call(
                func=Name(id='EscposDriver', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Subscript(
                    value=Attribute(
                        value=Name(id='proxy', ctx=Load()),
                        attr='proxy_drivers',
                        ctx=Load(),
                    ),
                    slice=Constant(value='escpos', kind=None),
                    ctx=Store(),
                ),
            ],
            value=Name(id='driver', ctx=Load()),
            type_comment=None,
        ),
        ClassDef(
            name='EscposProxy',
            bases=[
                Attribute(
                    value=Name(id='proxy', ctx=Load()),
                    attr='ProxyController',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='open_cashbox',
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ESC/POS: OPEN CASHBOX', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='driver', ctx=Load()),
                                    attr='push_task',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='cashbox', kind=None)],
                                keywords=[],
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
                            args=[Constant(value='/hw_proxy/open_cashbox', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='print_receipt',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='receipt', annotation=None, type_comment=None),
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ESC/POS: PRINT RECEIPT', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='driver', ctx=Load()),
                                    attr='push_task',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='receipt', kind=None),
                                    Name(id='receipt', ctx=Load()),
                                ],
                                keywords=[],
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
                            args=[Constant(value='/hw_proxy/print_receipt', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='print_xml_receipt',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='receipt', annotation=None, type_comment=None),
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ESC/POS: PRINT XML RECEIPT', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='driver', ctx=Load()),
                                    attr='push_task',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='xml_receipt', kind=None),
                                    Name(id='receipt', ctx=Load()),
                                ],
                                keywords=[],
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
                            args=[Constant(value='/hw_proxy/print_xml_receipt', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
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
