Module(
    body=[
        Import(
            names=[alias(name='ctypes', asname=None)],
        ),
        Import(
            names=[alias(name='evdev', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module='pathlib',
            names=[alias(name='Path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='queue',
            names=[
                alias(name='Queue', asname=None),
                alias(name='Empty', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        ImportFrom(
            module='threading',
            names=[alias(name='Lock', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='urllib3', asname=None)],
        ),
        ImportFrom(
            module='usb',
            names=[alias(name='util', asname=None)],
            level=0,
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
            targets=[Name(id='xlib', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Name(id='ctypes', ctx=Load()),
                        attr='cdll',
                        ctx=Load(),
                    ),
                    attr='LoadLibrary',
                    ctx=Load(),
                ),
                args=[Constant(value='libX11.so.6', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='KeyboardUSBDriver',
            bases=[Name(id='Driver', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='connection_type', ctx=Store())],
                    value=Constant(value='usb', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='keyboard_layout_groups', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='available_layouts', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='KeyboardUSBDriver', ctx=Load()),
                                        Constant(value='display', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='environ',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='XAUTHORITY', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='/run/lightdm/pi/xauthority', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                            attr='display',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='xlib', ctx=Load()),
                                            attr='XOpenDisplay',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='bytes', ctx=Load()),
                                                args=[
                                                    Constant(value=':0.0', kind=None),
                                                    Constant(value='utf-8', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='KeyboardUSBDriver', ctx=Load()),
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
                                    attr='device_connection',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='direct', kind=None),
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_name',
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
                                        attr='_actions',
                                        ctx=Load(),
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='update_layout', kind=None),
                                            Constant(value='update_is_scanner', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_update_layout',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_save_is_scanner',
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
                                    attr='_scancode_to_modifier',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value=42, kind=None),
                                    Constant(value=54, kind=None),
                                    Constant(value=58, kind=None),
                                    Constant(value=69, kind=None),
                                    Constant(value=100, kind=None),
                                ],
                                values=[
                                    Constant(value='left_shift', kind=None),
                                    Constant(value='right_shift', kind=None),
                                    Constant(value='caps_lock', kind=None),
                                    Constant(value='num_lock', kind=None),
                                    Constant(value='alt_gr', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_tracked_modifiers',
                                    ctx=Store(),
                                ),
                            ],
                            value=DictComp(
                                key=Name(id='modifier', ctx=Load()),
                                value=Constant(value=False, kind=None),
                                generators=[
                                    comprehension(
                                        target=Name(id='modifier', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_scancode_to_modifier',
                                                    ctx=Load(),
                                                ),
                                                attr='values',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                    attr='available_layouts',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                            attr='load_layouts_list',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                    attr='send_layouts_list',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='evdev_device', ctx=Store()),
                            iter=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='evdev', ctx=Load()),
                                        attr='InputDevice',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='path', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='path', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='evdev', ctx=Load()),
                                                attr='list_devices',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='device', ctx=Load()),
                                                    attr='idVendor',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='evdev_device', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        attr='vendor',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='device', ctx=Load()),
                                                    attr='idProduct',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='evdev_device', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        attr='product',
                                                        ctx=Load(),
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
                                                    attr='input_device',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='evdev_device', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_is_scanner',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_set_device_type',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='scanner', kind=None)],
                                    keywords=[],
                                ),
                                orelse=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_set_device_type',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
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
                        For(
                            target=Name(id='cfg', ctx=Store()),
                            iter=Name(id='device', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='itf', ctx=Store()),
                                    iter=Name(id='cfg', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='itf', ctx=Load()),
                                                            attr='bInterfaceClass',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=3, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='itf', ctx=Load()),
                                                            attr='bInterfaceProtocol',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value=2, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='device', ctx=Load()),
                                                            attr='interface_protocol',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='itf', ctx=Load()),
                                                        attr='bInterfaceProtocol',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
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
                            ],
                            orelse=[],
                            type_comment=None,
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
                            value=Constant(value='Allows `hw_proxy.Proxy` to retrieve the status of the scanners', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='any', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=Compare(
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
                                                comparators=[Constant(value='scanner', kind=None)],
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
                    name='send_layouts_list',
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
                            targets=[Name(id='server', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='get_odoo_server_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='server', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='urllib3', ctx=Load()),
                                            attr='disable_warnings',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='pm', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='urllib3', ctx=Load()),
                                            attr='PoolManager',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='cert_reqs',
                                                value=Constant(value='CERT_NONE', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='server', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='server', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value='/iot/keyboard_layouts', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pm', ctx=Load()),
                                                    attr='request',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='POST', kind=None),
                                                    Name(id='server', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='fields',
                                                        value=Dict(
                                                            keys=[Constant(value='available_layouts', kind=None)],
                                                            values=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='json', ctx=Load()),
                                                                        attr='dumps',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='available_layouts',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
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
                                                        args=[Constant(value='Could not reach configured server', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='A error encountered : %s ', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='e', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
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
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='load_layouts_list',
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
                            targets=[Name(id='tree', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='parse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/usr/share/X11/xkb/rules/base.xml', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='XMLParser',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='ns_clean',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='recover',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='layouts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//layout', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='layout', ctx=Store()),
                            iter=Name(id='layouts', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='layout_name', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='layout', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='./configItem/name', kind=None)],
                                                keywords=[],
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='layout_description', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='layout', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='./configItem/description', kind=None)],
                                                keywords=[],
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='text',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                                attr='available_layouts',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='layout', kind=None),
                                                ],
                                                values=[
                                                    Name(id='layout_description', ctx=Load()),
                                                    Name(id='layout_name', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='variant', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='layout', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='./variantList/variant', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='variant_name', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='variant', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='./configItem/name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='variant_description', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='variant', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='./configItem/description', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                                        attr='available_layouts',
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='layout', kind=None),
                                                            Constant(value='variant', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='variant_description', ctx=Load()),
                                                            Name(id='layout_name', ctx=Load()),
                                                            Name(id='variant_name', ctx=Load()),
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_name',
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
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='manufacturer', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='util', ctx=Load()),
                                            attr='get_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dev',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dev',
                                                    ctx=Load(),
                                                ),
                                                attr='iManufacturer',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='util', ctx=Load()),
                                            attr='get_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dev',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dev',
                                                    ctx=Load(),
                                                ),
                                                attr='iProduct',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=BinOp(
                                        left=Constant(value='%s - %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='manufacturer', ctx=Load()),
                                                Name(id='product', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Unknown input device', kind=None)],
                                                keywords=[],
                                            ),
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
                        Try(
                            body=[
                                For(
                                    target=Name(id='event', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='input_device',
                                                ctx=Load(),
                                            ),
                                            attr='read_loop',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_stopped',
                                                        ctx=Load(),
                                                    ),
                                                    attr='isSet',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='evdev', ctx=Load()),
                                                            attr='ecodes',
                                                            ctx=Load(),
                                                        ),
                                                        attr='EV_KEY',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='data', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='evdev', ctx=Load()),
                                                            attr='categorize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='event', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='modifier_name', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_scancode_to_modifier',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='data', ctx=Load()),
                                                                attr='scancode',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='modifier_name', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='modifier_name', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='caps_lock', kind=None),
                                                                            Constant(value='num_lock', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='data', ctx=Load()),
                                                                            attr='keystate',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value=1, kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='_tracked_modifiers',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Name(id='modifier_name', ctx=Load()),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=UnaryOp(
                                                                                op=Not(),
                                                                                operand=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='_tracked_modifiers',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Name(id='modifier_name', ctx=Load()),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            type_comment=None,
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
                                                                                attr='_tracked_modifiers',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Name(id='modifier_name', ctx=Load()),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Name(id='bool', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='data', ctx=Load()),
                                                                                attr='keystate',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='data', ctx=Load()),
                                                                    attr='keystate',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='key_input',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='data', ctx=Load()),
                                                                                attr='scancode',
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
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='err',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='err', ctx=Load())],
                                                keywords=[],
                                            ),
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
                    name='_change_keyboard_layout',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='new_layout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Change the layout of the current device to what is specified in\n        new_layout.\n\n        Args:\n            new_layout (dict): A dict containing two keys:\n                - layout (str): The layout code\n                - variant (str): An optional key to represent the variant of the\n                                 selected layout\n        ', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Constant(value='keyboard_layout', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                                attr='keyboard_layout_groups',
                                                ctx=Load(),
                                            ),
                                            attr='remove',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='keyboard_layout',
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
                            test=Name(id='new_layout', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='keyboard_layout',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='new_layout', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='layout', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='us', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='new_layout', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='variant', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='keyboard_layout',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value='(%s)', kind=None),
                                                op=Mod(),
                                                right=Subscript(
                                                    value=Name(id='new_layout', ctx=Load()),
                                                    slice=Constant(value='variant', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='keyboard_layout',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='us', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                        attr='keyboard_layout_groups',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='keyboard_layout',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='setxkbmap', kind=None),
                                            Constant(value='-display', kind=None),
                                            Constant(value=':0.0', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value=',', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                                        attr='keyboard_layout_groups',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xlib', ctx=Load()),
                                    attr='XCloseDisplay',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                        attr='display',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                    attr='display',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xlib', ctx=Load()),
                                    attr='XOpenDisplay',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='bytes', ctx=Load()),
                                        args=[
                                            Constant(value=':0.0', kind=None),
                                            Constant(value='utf-8', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_layout',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='layout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Save the layout to a file on the box to read it when restarting it.\n        We need that in order to keep the selected layout after a reboot.\n\n        Args:\n            new_layout (dict): A dict containing two keys:\n                - layout (str): The layout code\n                - variant (str): An optional key to represent the variant of the\n                                 selected layout\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='file_path', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='Path', ctx=Load()),
                                        attr='home',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Div(),
                                right=Constant(value='odoo-keyboard-layouts.conf', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='file_path', ctx=Load()),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='loads',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='file_path', ctx=Load()),
                                                    attr='read_text',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device_identifier',
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='layout', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='write_file',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='odoo-keyboard-layouts.conf', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
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
                FunctionDef(
                    name='load_layout',
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
                            value=Constant(value="Read the layout from the saved filed and set it as current layout.\n        If no file or no layout is found we use 'us' by default.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='file_path', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='Path', ctx=Load()),
                                        attr='home',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Div(),
                                right=Constant(value='odoo-keyboard-layouts.conf', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='file_path', ctx=Load()),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='loads',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='file_path', ctx=Load()),
                                                    attr='read_text',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='layout', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='device_identifier',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='layout', kind=None)],
                                                values=[Constant(value='us', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='layout', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='layout', kind=None)],
                                        values=[Constant(value='us', kind=None)],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_change_keyboard_layout',
                                    ctx=Load(),
                                ),
                                args=[Name(id='layout', ctx=Load())],
                                keywords=[],
                            ),
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='value', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
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
                    name='_is_scanner',
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
                            value=Constant(value='Read the device type from the saved filed and set it as current type.\n        If no file or no device type is found we try to detect it automatically.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='device_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device_name',
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
                            targets=[Name(id='scanner_name', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='barcode', kind=None),
                                    Constant(value='scanner', kind=None),
                                    Constant(value='reader', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_scanner', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='x', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[Name(id='device_name', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Name(id='scanner_name', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dev',
                                                ctx=Load(),
                                            ),
                                            attr='interface_protocol',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='0', kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='file_path', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='Path', ctx=Load()),
                                        attr='home',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Div(),
                                right=Constant(value='odoo-keyboard-is-scanner.conf', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='file_path', ctx=Load()),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='loads',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='file_path', ctx=Load()),
                                                    attr='read_text',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='is_scanner', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='device_identifier',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='is_scanner', kind=None),
                                            Name(id='is_scanner', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='is_scanner', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_keyboard_input',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='scancode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Deal with a keyboard input. Send the character corresponding to the\n        pressed key represented by its scancode to the connected Odoo instance.\n\n        Args:\n            scancode (int): The scancode of the pressed key.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='value', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_scancode_to_char',
                                    ctx=Load(),
                                ),
                                args=[Name(id='scancode', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='value', kind=None),
                                ctx=Load(),
                            ),
                            body=[
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
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_barcode_scanner_input',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='scancode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Deal with a barcode scanner input. Add the new character scanned to\n        the current barcode or complete the barcode if "Return" is pressed.\n        When a barcode is completed, two tasks are performed:\n            - Send a device_changed update to the event manager to notify the\n            listeners that the value has changed (used in Enterprise).\n            - Add the barcode to the list barcodes that are being queried in\n            Community.\n\n        Args:\n            scancode (int): The scancode of the pressed key.\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='scancode', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=28, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='value', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_current_barcode',
                                        ctx=Load(),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_barcodes',
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
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_current_barcode',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_current_barcode',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_current_barcode',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_scancode_to_char',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='scancode', ctx=Load())],
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
                    name='_save_is_scanner',
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
                            value=Constant(value='Save the type of device.\n        We need that in order to keep the selected type of device after a reboot.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='is_scanner', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='is_scanner', kind=None)],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='is_scanner', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='file_path', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='Path', ctx=Load()),
                                        attr='home',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Div(),
                                right=Constant(value='odoo-keyboard-is-scanner.conf', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='file_path', ctx=Load()),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='loads',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='file_path', ctx=Load()),
                                                    attr='read_text',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='device_identifier',
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='is_scanner', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='write_file',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='odoo-keyboard-is-scanner.conf', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='is_scanner', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='is_scanner', kind=None)],
                                    keywords=[],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_set_device_type',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='scanner', kind=None)],
                                    keywords=[],
                                ),
                                orelse=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_set_device_type',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_layout',
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
                            targets=[Name(id='layout', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='layout', kind=None),
                                    Constant(value='variant', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='layout', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='variant', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_change_keyboard_layout',
                                    ctx=Load(),
                                ),
                                args=[Name(id='layout', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='save_layout',
                                    ctx=Load(),
                                ),
                                args=[Name(id='layout', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_device_type',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='device_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='keyboard', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Modify the device type between 'keyboard' and 'scanner'\n\n        Args:\n            type (string): Type wanted to switch\n        ", kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='device_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='scanner', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='device_type',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='scanner', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='key_input',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_barcode_scanner_input',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_barcodes',
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
                                            attr='_current_barcode',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='input_device',
                                                ctx=Load(),
                                            ),
                                            attr='grab',
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
                                            attr='read_barcode_lock',
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
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='device_type',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='keyboard', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='key_input',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_keyboard_input',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='load_layout',
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
                    name='_scancode_to_char',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='scancode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Translate a received scancode to a character depending on the\n        selected keyboard layout and the current state of the keyboard's\n        modifiers.\n\n        Args:\n            scancode (int): The scancode of the pressed key, to be translated to\n                a character\n\n        Returns:\n            str: The translated scancode.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                        attr='keyboard_layout_groups',
                                        ctx=Load(),
                                    ),
                                    attr='index',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='keyboard_layout',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='modifiers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_active_modifiers',
                                    ctx=Load(),
                                ),
                                args=[Name(id='scancode', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='keysym', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ctypes', ctx=Load()),
                                    attr='c_int',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='xlib', ctx=Load()),
                                            attr='XkbKeycodeToKeysym',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                                attr='display',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Name(id='scancode', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=8, kind=None),
                                            ),
                                            Name(id='group', ctx=Load()),
                                            Name(id='modifiers', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='key_pressed', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ctypes', ctx=Load()),
                                    attr='create_string_buffer',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=5, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xlib', ctx=Load()),
                                    attr='XkbTranslateKeySym',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='KeyboardUSBDriver', ctx=Load()),
                                        attr='display',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ctypes', ctx=Load()),
                                            attr='byref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='keysym', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ctypes', ctx=Load()),
                                            attr='byref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='key_pressed', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ctypes', ctx=Load()),
                                            attr='byref',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ctypes', ctx=Load()),
                                                    attr='c_int',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='key_pressed', ctx=Load()),
                                attr='value',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='key_pressed', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value='', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_active_modifiers',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='scancode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Get the state of currently active modifiers.\n\n        Args:\n            scancode (int): The scancode of the key being translated\n\n        Returns:\n            int: The current state of the modifiers:\n                0 -- Lowercase\n                1 -- Highercase or (NumLock + key pressed on keypad)\n                2 -- AltGr\n                3 -- Highercase + AltGr\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='modifiers', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uppercase', ctx=Store())],
                            value=BinOp(
                                left=BoolOp(
                                    op=Or(),
                                    values=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_tracked_modifiers',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='right_shift', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_tracked_modifiers',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='left_shift', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                op=BitXor(),
                                right=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_tracked_modifiers',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='caps_lock', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='uppercase', ctx=Load()),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='scancode', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value=71, kind=None),
                                                            Constant(value=72, kind=None),
                                                            Constant(value=73, kind=None),
                                                            Constant(value=75, kind=None),
                                                            Constant(value=76, kind=None),
                                                            Constant(value=77, kind=None),
                                                            Constant(value=79, kind=None),
                                                            Constant(value=80, kind=None),
                                                            Constant(value=81, kind=None),
                                                            Constant(value=82, kind=None),
                                                            Constant(value=83, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_tracked_modifiers',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='num_lock', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='modifiers', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_tracked_modifiers',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='alt_gr', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='modifiers', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=2, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='modifiers', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='read_next_barcode',
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
                            value=Constant(value="Get the value of the last barcode that was scanned but not sent yet\n        and not older than 5 seconds. This function is used in Community, when\n        we don't have access to the IoTLongpolling.\n\n        Returns:\n            str: The next barcode to be read or an empty string.\n        ", kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='read_barcode_lock',
                                        ctx=Load(),
                                    ),
                                    attr='locked',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_barcodes',
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
                                                    Constant(value='', kind=None),
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='read_barcode_lock',
                                        ctx=Load(),
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='timestamp', ctx=Store()),
                                                        Name(id='barcode', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_barcodes',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=True, kind=None),
                                                    Constant(value=55, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='timestamp', ctx=Load()),
                                                ops=[Gt()],
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
                                                        right=Constant(value=5, kind=None),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Name(id='barcode', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Empty', ctx=Load()),
                                            name=None,
                                            body=[
                                                Return(
                                                    value=Constant(value='', kind=None),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
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
        Assign(
            targets=[
                Subscript(
                    value=Name(id='proxy_drivers', ctx=Load()),
                    slice=Constant(value='scanner', kind=None),
                    ctx=Store(),
                ),
            ],
            value=Name(id='KeyboardUSBDriver', ctx=Load()),
            type_comment=None,
        ),
        ClassDef(
            name='KeyboardUSBController',
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
                    name='get_barcode',
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
                            targets=[Name(id='scanners', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='iot_devices', ctx=Load()),
                                    slice=Name(id='d', ctx=Load()),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='d', ctx=Store()),
                                        iter=Name(id='iot_devices', ctx=Load()),
                                        ifs=[
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
                                                comparators=[Constant(value='scanner', kind=None)],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='scanners', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='scanners', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='read_next_barcode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/hw_proxy/scanner', kind=None)],
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
