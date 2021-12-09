Module(
    body=[
        Import(
            names=[alias(name='jinja2', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
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
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='urllib3', asname=None)],
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
            targets=[Name(id='path', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Name(id='os', ctx=Load()),
                        attr='path',
                        ctx=Load(),
                    ),
                    attr='realpath',
                    ctx=Load(),
                ),
                args=[
                    Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='dirname',
                                    ctx=Load(),
                                ),
                                args=[Name(id='__file__', ctx=Load())],
                                keywords=[],
                            ),
                            Constant(value='../../views', kind=None),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='loader', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja2', ctx=Load()),
                    attr='FileSystemLoader',
                    ctx=Load(),
                ),
                args=[Name(id='path', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='jinja_env', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja2', ctx=Load()),
                    attr='Environment',
                    ctx=Load(),
                ),
                args=[],
                keywords=[
                    keyword(
                        arg='loader',
                        value=Name(id='loader', ctx=Load()),
                    ),
                    keyword(
                        arg='autoescape',
                        value=Constant(value=True, kind=None),
                    ),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Subscript(
                    value=Attribute(
                        value=Name(id='jinja_env', ctx=Load()),
                        attr='filters',
                        ctx=Load(),
                    ),
                    slice=Constant(value='json', kind=None),
                    ctx=Store(),
                ),
            ],
            value=Attribute(
                value=Name(id='json', ctx=Load()),
                attr='dumps',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='pos_display_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='pos_display.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
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
            name='DisplayDriver',
            bases=[Name(id='Driver', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='connection_type', ctx=Store())],
                    value=Constant(value='display', kind=None),
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
                                            Name(id='DisplayDriver', ctx=Load()),
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
                            value=Constant(value='display', kind=None),
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
                            value=Constant(value='hdmi', kind=None),
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
                                slice=Constant(value='name', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='event_data',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='Event',
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
                                    attr='owner',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rendered_html',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device_identifier',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='distant_display', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_x_screen',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='device', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='x_screen', kind=None),
                                            Constant(value='0', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='load_url',
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
                                            Constant(value='update_url', kind=None),
                                            Constant(value='display_refresh', kind=None),
                                            Constant(value='take_control', kind=None),
                                            Constant(value='customer_facing_display', kind=None),
                                            Constant(value='get_owner', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_action_update_url',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_action_display_refresh',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_action_take_control',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_action_customer_facing_display',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_action_get_owner',
                                                ctx=Load(),
                                            ),
                                        ],
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
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_default_display',
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
                            targets=[Name(id='displays', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='filter', ctx=Load()),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='d', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
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
                                                    comparators=[Constant(value='display', kind=None)],
                                                ),
                                            ),
                                            Name(id='iot_devices', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='displays', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Name(id='iot_devices', ctx=Load()),
                                        slice=Subscript(
                                            value=Name(id='displays', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
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
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='device_identifier',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='distant_display', kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
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
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='sleep',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=60, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='url',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            BinOp(
                                                left=Constant(value='http://localhost:8069/point_of_sale/display/', kind=None),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='device_identifier',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='call_xdotools',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='F5', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                    name='update_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
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
                                    slice=Constant(value='DISPLAY', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value=':0.', kind=None),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_x_screen',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
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
                            targets=[Name(id='firefox_env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
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
                                    value=Name(id='firefox_env', ctx=Load()),
                                    slice=Constant(value='HOME', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value='/tmp/', kind=None),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_x_screen',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='url', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='http://localhost:8069/point_of_sale/display/', kind=None),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='device_identifier',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_window', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='xdotool', kind=None),
                                            Constant(value='search', kind=None),
                                            Constant(value='--onlyvisible', kind=None),
                                            Constant(value='--screen', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_x_screen',
                                                ctx=Load(),
                                            ),
                                            Constant(value='--class', kind=None),
                                            Constant(value='Firefox', kind=None),
                                        ],
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
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='Popen',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='firefox', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='env',
                                        value=Name(id='firefox_env', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=Name(id='new_window', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='call_xdotools',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='F11', kind=None)],
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
                    name='load_url',
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
                            targets=[Name(id='url', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='get_odoo_server_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                    targets=[Name(id='http', ctx=Store())],
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
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='http', ctx=Load()),
                                                    attr='request',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='GET', kind=None),
                                                    BinOp(
                                                        left=Constant(value='%s/iot/box/%s/display_url', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='helpers', ctx=Load()),
                                                                        attr='get_odoo_server_url',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='helpers', ctx=Load()),
                                                                        attr='get_mac_address',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='status',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=200, kind=None)],
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
                                                                    value=Attribute(
                                                                        value=Name(id='response', ctx=Load()),
                                                                        attr='data',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='decode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='utf8', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='url', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='device_identifier',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='decoder',
                                                    ctx=Load(),
                                                ),
                                                attr='JSONDecodeError',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='url', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='response', ctx=Load()),
                                                                attr='data',
                                                                ctx=Load(),
                                                            ),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='utf8', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='update_url',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='call_xdotools',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='keystroke', annotation=None, type_comment=None),
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
                                        value=Name(id='os', ctx=Load()),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='DISPLAY', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value=':0.', kind=None),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_x_screen',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
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
                        Try(
                            body=[
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
                                                    Constant(value='xdotool', kind=None),
                                                    Constant(value='search', kind=None),
                                                    Constant(value='--sync', kind=None),
                                                    Constant(value='--onlyvisible', kind=None),
                                                    Constant(value='--screen', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_x_screen',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='--class', kind=None),
                                                    Constant(value='Firefox', kind=None),
                                                    Constant(value='key', kind=None),
                                                    Name(id='keystroke', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=BinOp(
                                        left=Constant(value='xdotool succeeded in stroking ', kind=None),
                                        op=Add(),
                                        right=Name(id='keystroke', ctx=Load()),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value='xdotool threw an error, maybe it is not installed on the IoTBox', kind=None),
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
                    name='update_customer_facing_display',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='origin', annotation=None, type_comment=None),
                            arg(arg='html', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='origin', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='owner',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='rendered_html',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='html', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='event_data',
                                                ctx=Load(),
                                            ),
                                            attr='set',
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
                    name='get_serialized_order',
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='event_data',
                                        ctx=Load(),
                                    ),
                                    attr='wait',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=28, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='event_data',
                                                ctx=Load(),
                                            ),
                                            attr='clear',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='rendered_html', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='rendered_html',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='rendered_html', kind=None)],
                                values=[Constant(value=False, kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='take_control',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='new_owner', annotation=None, type_comment=None),
                            arg(arg='html', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='owner',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='new_owner', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rendered_html',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='html', ctx=Load()),
                            type_comment=None,
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
                                    Constant(value='owner', kind=None),
                                ],
                                values=[
                                    Constant(value='', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='owner',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='event_data',
                                        ctx=Load(),
                                    ),
                                    attr='set',
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
                    name='_action_update_url',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device_identifier',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='distant_display', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='update_url',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='url', kind=None)],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_action_display_refresh',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device_identifier',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='distant_display', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='call_xdotools',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='F5', kind=None)],
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
                    name='_action_take_control',
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
                                    attr='take_control',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='data',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='owner', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='html', kind=None)],
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
                    name='_action_customer_facing_display',
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
                                    attr='update_customer_facing_display',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='data',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='owner', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='html', kind=None)],
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
                    name='_action_get_owner',
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
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='data',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='value', kind=None),
                                    Constant(value='owner', kind=None),
                                ],
                                values=[
                                    Constant(value='', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='owner',
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='DisplayController',
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
                    name='display_refresh',
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
                            targets=[Name(id='display', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='DisplayDriver', ctx=Load()),
                                    attr='get_default_display',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='display', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='display', ctx=Load()),
                                            attr='device_identifier',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='distant_display', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='display', ctx=Load()),
                                            attr='call_xdotools',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='F5', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/hw_proxy/display_refresh', kind=None)],
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
                    name='customer_facing_display',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='html', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='display', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='DisplayDriver', ctx=Load()),
                                    attr='get_default_display',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='display', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='display', ctx=Load()),
                                            attr='update_customer_facing_display',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='http', ctx=Load()),
                                                        attr='request',
                                                        ctx=Load(),
                                                    ),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='remote_addr',
                                                ctx=Load(),
                                            ),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='status', kind=None)],
                                        values=[Constant(value='updated', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='status', kind=None)],
                                values=[Constant(value='failed', kind=None)],
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
                            args=[Constant(value='/hw_proxy/customer_facing_display', kind=None)],
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
                    name='take_control',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='html', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='display', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='DisplayDriver', ctx=Load()),
                                    attr='get_default_display',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='display', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='display', ctx=Load()),
                                            attr='take_control',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='http', ctx=Load()),
                                                        attr='request',
                                                        ctx=Load(),
                                                    ),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='remote_addr',
                                                ctx=Load(),
                                            ),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='status', kind=None),
                                            Constant(value='message', kind=None),
                                        ],
                                        values=[
                                            Constant(value='success', kind=None),
                                            Constant(value='You now have access to the display', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/hw_proxy/take_control', kind=None)],
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
                    name='test_ownership',
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
                            targets=[Name(id='display', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='DisplayDriver', ctx=Load()),
                                    attr='get_default_display',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='display', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='display', ctx=Load()),
                                            attr='owner',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='http', ctx=Load()),
                                                        attr='request',
                                                        ctx=Load(),
                                                    ),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='remote_addr',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='status', kind=None)],
                                        values=[Constant(value='OWNER', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='status', kind=None)],
                                values=[Constant(value='NOWNER', kind=None)],
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
                            args=[Constant(value='/hw_proxy/test_ownership', kind=None)],
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
                    name='get_serialized_order',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='display_identifier', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Name(id='display_identifier', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='display', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='iot_devices', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='display_identifier', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='display', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='DisplayDriver', ctx=Load()),
                                            attr='get_default_display',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='display', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='display', ctx=Load()),
                                            attr='get_serialized_order',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='rendered_html', kind=None),
                                    Constant(value='error', kind=None),
                                ],
                                values=[
                                    Constant(value=False, kind=None),
                                    Constant(value='No display found', kind=None),
                                ],
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
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/point_of_sale/get_serialized_order', kind=None),
                                        Constant(value='/point_of_sale/get_serialized_order/<string:display_identifier>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='display',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='display_identifier', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cust_js', ctx=Store())],
                            value=Constant(value=None, kind=None),
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='dirname',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='__file__', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='../../static/src/js/worker.js', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='js', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='cust_js', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='js', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='display_ifaces', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='iface_id', ctx=Store()),
                            iter=Name(id='interfaces', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Constant(value='wlan', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='iface_id', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='eth', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='iface_id', ctx=Load())],
                                            ),
                                        ],
                                    ),
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
                                        Assign(
                                            targets=[Name(id='essid', ctx=Store())],
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
                                        For(
                                            target=Name(id='conf', ctx=Store()),
                                            iter=Name(id='ifconfigs', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='conf', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='addr', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='display_ifaces', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='iface_id', kind=None),
                                                                            Constant(value='essid', kind=None),
                                                                            Constant(value='addr', kind=None),
                                                                            Constant(value='icon', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Name(id='iface_id', ctx=Load()),
                                                                            Name(id='essid', ctx=Load()),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='conf', ctx=Load()),
                                                                                    attr='get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='addr', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            IfExp(
                                                                                test=Compare(
                                                                                    left=Constant(value='eth', kind=None),
                                                                                    ops=[In()],
                                                                                    comparators=[Name(id='iface_id', ctx=Load())],
                                                                                ),
                                                                                body=Constant(value='sitemap', kind=None),
                                                                                orelse=Constant(value='wifi', kind=None),
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
                                            ],
                                            orelse=[],
                                            type_comment=None,
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
                                operand=Name(id='display_identifier', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='display_identifier', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='DisplayDriver', ctx=Load()),
                                                attr='get_default_display',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='device_identifier',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pos_display_template', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='breadcrumb', kind=None),
                                            Constant(value='cust_js', kind=None),
                                            Constant(value='display_ifaces', kind=None),
                                            Constant(value='display_identifier', kind=None),
                                            Constant(value='pairing_code', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Odoo -- Point of Sale', kind=None),
                                            Constant(value='POS Client display', kind=None),
                                            Name(id='cust_js', ctx=Load()),
                                            Name(id='display_ifaces', ctx=Load()),
                                            Name(id='display_identifier', ctx=Load()),
                                            Attribute(
                                                value=Name(id='connection_manager', ctx=Load()),
                                                attr='pairing_code',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
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
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/point_of_sale/display', kind=None),
                                        Constant(value='/point_of_sale/display/<string:display_identifier>', kind=None),
                                    ],
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
                                    value=Constant(value='none', kind=None),
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
