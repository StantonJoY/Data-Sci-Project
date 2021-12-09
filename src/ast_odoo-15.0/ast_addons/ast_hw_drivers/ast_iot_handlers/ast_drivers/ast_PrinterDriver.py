Module(
    body=[
        ImportFrom(
            module='base64',
            names=[alias(name='b64decode', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='cups',
            names=[
                alias(name='IPPError', asname=None),
                alias(name='IPP_PRINTER_IDLE', asname=None),
                alias(name='IPP_PRINTER_PROCESSING', asname=None),
                alias(name='IPP_PRINTER_STOPPED', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='dbus', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='netifaces', asname='ni')],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module='PIL',
            names=[
                alias(name='Image', asname=None),
                alias(name='ImageOps', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        ImportFrom(
            module='uuid',
            names=[alias(name='getnode', asname='get_mac')],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.connection_manager',
            names=[alias(name='connection_manager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.controllers.proxy',
            names=[alias(name='proxy_drivers', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.driver',
            names=[alias(name='Driver', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.event_manager',
            names=[alias(name='event_manager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.iot_handlers.interfaces.PrinterInterface',
            names=[
                alias(name='PPDs', asname=None),
                alias(name='conn', asname=None),
                alias(name='cups_lock', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.main',
            names=[alias(name='iot_devices', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.tools',
            names=[alias(name='helpers', asname=None)],
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
        Assign(
            targets=[Name(id='RECEIPT_PRINTER_COMMANDS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='star', kind=None),
                    Constant(value='escpos', kind=None),
                ],
                values=[
                    Dict(
                        keys=[
                            Constant(value='center', kind=None),
                            Constant(value='cut', kind=None),
                            Constant(value='title', kind=None),
                            Constant(value='drawers', kind=None),
                        ],
                        values=[
                            Constant(value=b'\x1b\x1da\x01', kind=None),
                            Constant(value=b'\x1bd\x02', kind=None),
                            Constant(value=b'\x1bi\x01\x01%s\x1bi\x00\x00', kind=None),
                            List(
                                elts=[
                                    Constant(value=b'\x07', kind=None),
                                    Constant(value=b'\x1a', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    Dict(
                        keys=[
                            Constant(value='center', kind=None),
                            Constant(value='cut', kind=None),
                            Constant(value='title', kind=None),
                            Constant(value='drawers', kind=None),
                        ],
                        values=[
                            Constant(value=b'\x1ba\x01', kind=None),
                            Constant(value=b'\x1dVA\n', kind=None),
                            Constant(value=b'\x1b!0%s\x1b!\x00', kind=None),
                            List(
                                elts=[
                                    Constant(value=b'\x1b=\x01', kind=None),
                                    Constant(value=b'\x1bp\x00\x19\x19', kind=None),
                                    Constant(value=b'\x1bp\x01\x19\x19', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                ],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='cups_notification_handler',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='message', annotation=None, type_comment=None),
                    arg(arg='uri', annotation=None, type_comment=None),
                    arg(arg='device_identifier', annotation=None, type_comment=None),
                    arg(arg='state', annotation=None, type_comment=None),
                    arg(arg='reason', annotation=None, type_comment=None),
                    arg(arg='accepting_jobs', annotation=None, type_comment=None),
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
                        left=Name(id='device_identifier', ctx=Load()),
                        ops=[In()],
                        comparators=[Name(id='iot_devices', ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='reason', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='reason', ctx=Load()),
                                    ops=[NotEq()],
                                    comparators=[Constant(value='none', kind=None)],
                                ),
                                body=Name(id='reason', ctx=Load()),
                                orelse=Constant(value=None, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='state_value', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Name(id='IPP_PRINTER_IDLE', ctx=Load()),
                                    Name(id='IPP_PRINTER_PROCESSING', ctx=Load()),
                                    Name(id='IPP_PRINTER_STOPPED', ctx=Load()),
                                ],
                                values=[
                                    Constant(value='connected', kind=None),
                                    Constant(value='processing', kind=None),
                                    Constant(value='stopped', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='iot_devices', ctx=Load()),
                                        slice=Name(id='device_identifier', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='update_status',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='state_value', ctx=Load()),
                                        slice=Name(id='state', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Name(id='message', ctx=Load()),
                                    Name(id='reason', ctx=Load()),
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
        Try(
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='conn', ctx=Load()),
                            attr='getSubscriptions',
                            ctx=Load(),
                        ),
                        args=[Constant(value='/printers/', kind=None)],
                        keywords=[],
                    ),
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='IPPError', ctx=Load()),
                    name=None,
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='conn', ctx=Load()),
                                    attr='createSubscription',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='uri',
                                        value=Constant(value='/printers/', kind=None),
                                    ),
                                    keyword(
                                        arg='recipient_uri',
                                        value=Constant(value='dbus://', kind=None),
                                    ),
                                    keyword(
                                        arg='events',
                                        value=List(
                                            elts=[Constant(value='printer-state-changed', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Assign(
            targets=[Name(id='bus', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='dbus', ctx=Load()),
                    attr='SystemBus',
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
                    value=Name(id='bus', ctx=Load()),
                    attr='add_signal_receiver',
                    ctx=Load(),
                ),
                args=[Name(id='cups_notification_handler', ctx=Load())],
                keywords=[
                    keyword(
                        arg='signal_name',
                        value=Constant(value='PrinterStateChanged', kind=None),
                    ),
                    keyword(
                        arg='dbus_interface',
                        value=Constant(value='org.cups.cupsd.Notifier', kind=None),
                    ),
                ],
            ),
        ),
        ClassDef(
            name='PrinterDriver',
            bases=[Name(id='Driver', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='connection_type', ctx=Store())],
                    value=Constant(value='printer', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='identifier', annotation=None, type_comment=None),
                            arg(arg='device', annotation=None, type_comment=None),
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PrinterDriver', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='identifier', ctx=Load()),
                                    Name(id='device', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='printer', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device_connection',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='device', ctx=Load()),
                                        slice=Constant(value='device-class', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='lower',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device_name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='device', ctx=Load()),
                                slice=Constant(value='device-make-and-model', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='status', kind=None),
                                    Constant(value='message', kind=None),
                                    Constant(value='reason', kind=None),
                                ],
                                values=[
                                    Constant(value='connecting', kind=None),
                                    Constant(value='Connecting to printer', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='send_status',
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
                                        attr='_actions',
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='cashbox', kind=None),
                                            Constant(value='print_receipt', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='open_cashbox',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='print_receipt',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_action_default',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='receipt_protocol',
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Compare(
                                    left=Constant(value='STR_T', kind=None),
                                    ops=[In()],
                                    comparators=[
                                        Subscript(
                                            value=Name(id='device', ctx=Load()),
                                            slice=Constant(value='device-id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Constant(value='star', kind=None),
                                orelse=Constant(value='escpos', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='direct', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device_connection',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='cmd', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Name(id='device', ctx=Load()),
                                                            slice=Constant(value='device-id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='cmd', ctx=Store()),
                                                        iter=List(
                                                            elts=[
                                                                Constant(value='CMD:STAR;', kind=None),
                                                                Constant(value='CMD:ESC/POS;', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='print_status',
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
                FunctionDef(
                    name='supported',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
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
                            test=Call(
                                func=Attribute(
                                    value=Name(id='device', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='supported', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='protocol', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='dnssd', kind=None),
                                    Constant(value='lpd', kind=None),
                                    Constant(value='socket', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Name(id='x', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                Subscript(
                                                                    value=Name(id='device', ctx=Load()),
                                                                    slice=Constant(value='url', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='x', ctx=Store()),
                                                                iter=Name(id='protocol', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='device', ctx=Load()),
                                                    slice=Constant(value='device-make-and-model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='Unknown', kind=None)],
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Constant(value='direct', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='device', ctx=Load()),
                                                slice=Constant(value='device-class', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='get_device_model',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='device', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ppdFile', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='ppd', ctx=Store()),
                                    iter=Name(id='PPDs', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='model', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='model', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='PPDs', ctx=Load()),
                                                                    slice=Name(id='ppd', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ppd-product', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ppdFile', ctx=Store())],
                                                    value=Name(id='ppd', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Break(),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Name(id='cups_lock', ctx=Load()),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        If(
                                            test=Name(id='ppdFile', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='conn', ctx=Load()),
                                                            attr='addPrinter',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='name',
                                                                value=Subscript(
                                                                    value=Name(id='device', ctx=Load()),
                                                                    slice=Constant(value='identifier', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='ppdname',
                                                                value=Name(id='ppdFile', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='device',
                                                                value=Subscript(
                                                                    value=Name(id='device', ctx=Load()),
                                                                    slice=Constant(value='url', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='conn', ctx=Load()),
                                                            attr='addPrinter',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='name',
                                                                value=Subscript(
                                                                    value=Name(id='device', ctx=Load()),
                                                                    slice=Constant(value='identifier', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='device',
                                                                value=Subscript(
                                                                    value=Name(id='device', ctx=Load()),
                                                                    slice=Constant(value='url', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='conn', ctx=Load()),
                                                    attr='setPrinterInfo',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='device', ctx=Load()),
                                                        slice=Constant(value='identifier', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='device', ctx=Load()),
                                                        slice=Constant(value='device-make-and-model', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='conn', ctx=Load()),
                                                    attr='enablePrinter',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='device', ctx=Load()),
                                                        slice=Constant(value='identifier', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='conn', ctx=Load()),
                                                    attr='acceptJobs',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='device', ctx=Load()),
                                                        slice=Constant(value='identifier', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='conn', ctx=Load()),
                                                    attr='setPrinterUsersAllowed',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='device', ctx=Load()),
                                                        slice=Constant(value='identifier', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Constant(value='all', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='conn', ctx=Load()),
                                                    attr='addPrinterOptionDefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='device', ctx=Load()),
                                                        slice=Constant(value='identifier', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='usb-no-reattach', kind=None),
                                                    Constant(value='true', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='conn', ctx=Load()),
                                                    attr='addPrinterOptionDefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='device', ctx=Load()),
                                                        slice=Constant(value='identifier', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='usb-unidir', kind=None),
                                                    Constant(value='true', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_device_model',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='device', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='device_model', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='device', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='device-id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='device_id', ctx=Store()),
                                    iter=ListComp(
                                        elt=Name(id='device_lo', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='device_lo', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='device', ctx=Load()),
                                                            slice=Constant(value='device-id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=';', kind=None)],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Name(id='x', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[Name(id='device_id', ctx=Load())],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='x', ctx=Store()),
                                                                iter=List(
                                                                    elts=[
                                                                        Constant(value='MDL', kind=None),
                                                                        Constant(value='MODEL', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='device_model', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='device_id', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=':', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
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
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='device', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='device-make-and-model', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='device_model', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='device', ctx=Load()),
                                                slice=Constant(value='device-make-and-model', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='[\\(].*?[\\)]', kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='device_model', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_status',
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
                            targets=[Name(id='status', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='any', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='iot_devices', ctx=Load()),
                                                                slice=Name(id='d', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='device_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='printer', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='iot_devices', ctx=Load()),
                                                                slice=Name(id='d', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='device_connection',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='direct', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='d', ctx=Store()),
                                                    iter=Name(id='iot_devices', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                body=Constant(value='connected', kind=None),
                                orelse=Constant(value='disconnected', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='status', kind=None),
                                    Constant(value='messages', kind=None),
                                ],
                                values=[
                                    Name(id='status', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='disconnect',
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
                                    attr='update_status',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='disconnected', kind=None),
                                    Constant(value='Printer was disconnected', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PrinterDriver', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='disconnect',
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
                    name='update_status',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='reason', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Updates the state of the current printer.\n\n        Args:\n            status (str): The new value of the status\n            message (str): A comprehensive message describing the status\n            reason (str): The reason fo the current status\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='status', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='status', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='reason', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='reason', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='state',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='status', kind=None),
                                            Constant(value='message', kind=None),
                                            Constant(value='reason', kind=None),
                                        ],
                                        values=[
                                            Name(id='status', ctx=Load()),
                                            Name(id='message', ctx=Load()),
                                            Name(id='reason', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='send_status',
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
                FunctionDef(
                    name='send_status',
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
                            value=Constant(value=' Sends the current status of the printer to the connected Odoo instance.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='data',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='value', kind=None),
                                    Constant(value='state', kind=None),
                                ],
                                values=[
                                    Constant(value='', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event_manager', ctx=Load()),
                                    attr='device_changed',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='print_raw',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='process', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='Popen',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='lp', kind=None),
                                            Constant(value='-d', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device_identifier',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='stdin',
                                        value=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='PIPE',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='process', ctx=Load()),
                                    attr='communicate',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='print_receipt',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='receipt', ctx=Store())],
                            value=Call(
                                func=Name(id='b64decode', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='receipt', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='im', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='receipt', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='im', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='im', ctx=Load()),
                                    attr='convert',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='L', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='im', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ImageOps', ctx=Load()),
                                    attr='invert',
                                    ctx=Load(),
                                ),
                                args=[Name(id='im', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='im', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='im', ctx=Load()),
                                    attr='convert',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='1', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='print_command', ctx=Store())],
                            value=Call(
                                func=Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='self', ctx=Load()),
                                        BinOp(
                                            left=Constant(value='format_%s', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='receipt_protocol',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                args=[Name(id='im', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='print_raw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='print_command', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='format_star',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='im', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='width', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='im', ctx=Load()),
                                                attr='width',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=7, kind=None),
                                        ),
                                        op=Div(),
                                        right=Constant(value=8, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='raster_init', ctx=Store())],
                            value=Constant(value=b'\x1b*rA', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='raster_page_length', ctx=Store())],
                            value=Constant(value=b'\x1b*rP0\x00', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='raster_send', ctx=Store())],
                            value=Constant(value=b'b', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='raster_close', ctx=Store())],
                            value=Constant(value=b'\x1b*rB', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='raster_data', ctx=Store())],
                            value=Constant(value=b'', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dots', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='im', ctx=Load()),
                                    attr='tobytes',
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
                                args=[Name(id='dots', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='raster_data', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=BinOp(
                                            left=Name(id='raster_send', ctx=Load()),
                                            op=Add(),
                                            right=Call(
                                                func=Attribute(
                                                    value=Name(id='width', ctx=Load()),
                                                    attr='to_bytes',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='little', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Name(id='dots', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Name(id='width', ctx=Load()),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='dots', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='dots', ctx=Load()),
                                        slice=Slice(
                                            lower=Name(id='width', ctx=Load()),
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
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=Name(id='raster_init', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='raster_page_length', ctx=Load()),
                                    ),
                                    op=Add(),
                                    right=Name(id='raster_data', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='raster_close', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='format_escpos',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='im', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='width', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='im', ctx=Load()),
                                                attr='width',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=7, kind=None),
                                        ),
                                        op=Div(),
                                        right=Constant(value=8, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='raster_send', ctx=Store())],
                            value=Constant(value=b'\x1dv0\x00', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='max_slice_height', ctx=Store())],
                            value=Constant(value=255, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='raster_data', ctx=Store())],
                            value=Constant(value=b'', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dots', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='im', ctx=Load()),
                                    attr='tobytes',
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
                                args=[Name(id='dots', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='im_slice', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='dots', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=BinOp(
                                                left=Name(id='width', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='max_slice_height', ctx=Load()),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='slice_height', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='im_slice', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Div(),
                                                right=Name(id='width', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='raster_data', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Name(id='raster_send', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='width', ctx=Load()),
                                                        attr='to_bytes',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value=2, kind=None),
                                                        Constant(value='little', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            op=Add(),
                                            right=Call(
                                                func=Attribute(
                                                    value=Name(id='slice_height', ctx=Load()),
                                                    attr='to_bytes',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='little', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Name(id='im_slice', ctx=Load()),
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='dots', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='dots', ctx=Load()),
                                        slice=Slice(
                                            lower=BinOp(
                                                left=Name(id='width', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='max_slice_height', ctx=Load()),
                                            ),
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
                        Return(
                            value=BinOp(
                                left=Name(id='raster_data', ctx=Load()),
                                op=Add(),
                                right=Subscript(
                                    value=Subscript(
                                        value=Name(id='RECEIPT_PRINTER_COMMANDS', ctx=Load()),
                                        slice=Constant(value='escpos', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='cut', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='print_status',
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
                            value=Constant(value='Prints the status ticket of the IoTBox on the current printer.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='wlan', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ip', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mac', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='homepage', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pairing_code', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ssid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='get_ssid',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wlan', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='\nWireless network:\n%s\n\n', kind=None),
                                op=Mod(),
                                right=Name(id='ssid', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='interfaces', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ni', ctx=Load()),
                                    attr='interfaces',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ips', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='iface_id', ctx=Store()),
                            iter=Name(id='interfaces', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='iface_obj', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ni', ctx=Load()),
                                            attr='ifaddresses',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='iface_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ifconfigs', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='iface_obj', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='ni', ctx=Load()),
                                                attr='AF_INET',
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='conf', ctx=Store()),
                                    iter=Name(id='ifconfigs', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='conf', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='addr', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='conf', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='addr', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ips', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='conf', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='addr', kind=None)],
                                                                keywords=[],
                                                            ),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='ips', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ip', ctx=Store())],
                                    value=Constant(value='\nERROR: Could not connect to LAN\n\nPlease check that the IoTBox is correc-\ntly connected with a network cable,\n that the LAN is setup with DHCP, and\nthat network addresses are available', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='ips', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='ip', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='\nIP Address:\n%s\n', kind=None),
                                                op=Mod(),
                                                right=Subscript(
                                                    value=Name(id='ips', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='ip', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='\nIP Addresses:\n%s\n', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Constant(value='\n', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='ips', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='ips', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[GtE()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ips_filtered', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='i', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='i', ctx=Store()),
                                                iter=Name(id='ips', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='i', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='127.0.0.1', kind=None)],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='main_ips', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='ips_filtered', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='ips_filtered', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value='127.0.0.1', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mac', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='\nMAC Address:\n%s\n', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='helpers', ctx=Load()),
                                                attr='get_mac_address',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='homepage', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='\nHomepage:\nhttp://%s:8069\n\n', kind=None),
                                        op=Mod(),
                                        right=Name(id='main_ips', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Attribute(
                                value=Name(id='connection_manager', ctx=Load()),
                                attr='pairing_code',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='code', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='pairing_code', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='\nPairing Code:\n%s\n', kind=None),
                                        op=Mod(),
                                        right=Name(id='code', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='commands', ctx=Store())],
                            value=Subscript(
                                value=Name(id='RECEIPT_PRINTER_COMMANDS', ctx=Load()),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='receipt_protocol',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='title', ctx=Store())],
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='commands', ctx=Load()),
                                    slice=Constant(value='title', kind=None),
                                    ctx=Load(),
                                ),
                                op=Mod(),
                                right=Constant(value=b'IoTBox Status', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='print_raw',
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
                                                                    left=Subscript(
                                                                        value=Name(id='commands', ctx=Load()),
                                                                        slice=Constant(value='center', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Name(id='title', ctx=Load()),
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value=b'\n', kind=None),
                                                            ),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Attribute(
                                                                    value=Name(id='wlan', ctx=Load()),
                                                                    attr='encode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='mac', ctx=Load()),
                                                                attr='encode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Attribute(
                                                            value=Name(id='ip', ctx=Load()),
                                                            attr='encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='homepage', ctx=Load()),
                                                        attr='encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            op=Add(),
                                            right=Call(
                                                func=Attribute(
                                                    value=Name(id='pairing_code', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Name(id='commands', ctx=Load()),
                                            slice=Constant(value='cut', kind=None),
                                            ctx=Load(),
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
                FunctionDef(
                    name='open_cashbox',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Sends a signal to the current printer to open the connected cashbox.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='commands', ctx=Store())],
                            value=Subscript(
                                value=Name(id='RECEIPT_PRINTER_COMMANDS', ctx=Load()),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='receipt_protocol',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='drawer', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='commands', ctx=Load()),
                                slice=Constant(value='drawers', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='print_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='drawer', ctx=Load())],
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
                FunctionDef(
                    name='_action_default',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='print_raw',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='b64decode', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='document', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
        ClassDef(
            name='PrinterController',
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
                    name='default_printer_action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='printer', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='d', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='d', ctx=Store()),
                                                iter=Name(id='iot_devices', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='iot_devices', ctx=Load()),
                                                                        slice=Name(id='d', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='device_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='printer', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='iot_devices', ctx=Load()),
                                                                        slice=Name(id='d', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='device_connection',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='direct', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='printer', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='iot_devices', ctx=Load()),
                                                slice=Name(id='printer', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='action',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/hw_proxy/default_printer_action', kind=None)],
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
        Assign(
            targets=[
                Subscript(
                    value=Name(id='proxy_drivers', ctx=Load()),
                    slice=Constant(value='printer', kind=None),
                    ctx=Store(),
                ),
            ],
            value=Name(id='PrinterDriver', ctx=Load()),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
