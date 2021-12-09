Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='jinja2', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module='pathlib',
            names=[alias(name='Path', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='socket', asname=None)],
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='Response', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_resource_path', asname=None)],
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
        ImportFrom(
            module='odoo.addons.web.controllers',
            names=[alias(name='main', asname='web')],
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
        If(
            test=Call(
                func=Name(id='hasattr', ctx=Load()),
                args=[
                    Name(id='sys', ctx=Load()),
                    Constant(value='frozen', kind=None),
                ],
                keywords=[],
            ),
            body=[
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
                                    Constant(value='..', kind=None),
                                    Constant(value='views', kind=None),
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
            ],
            orelse=[
                Assign(
                    targets=[Name(id='loader', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='jinja2', ctx=Load()),
                            attr='PackageLoader',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='odoo.addons.hw_posbox_homepage', kind=None),
                            Constant(value='views', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
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
            targets=[Name(id='homepage_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='homepage.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='server_config_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='server_config.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='wifi_config_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='wifi_config.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='handler_list_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='handler_list.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='remote_connect_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='remote_connect.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='configure_wizard_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='configure_wizard.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='six_payment_terminal_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='six_payment_terminal.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='list_credential_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='list_credential.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='upgrade_page_template', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='jinja_env', ctx=Load()),
                    attr='get_template',
                    ctx=Load(),
                ),
                args=[Constant(value='upgrade_page.html', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='IoTboxHomepage',
            bases=[
                Attribute(
                    value=Name(id='web', ctx=Load()),
                    attr='Home',
                    ctx=Load(),
                ),
            ],
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IoTboxHomepage', ctx=Load()),
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
                                    attr='updating',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='Lock',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    name='clean_partition',
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
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='sudo', kind=None),
                                            Constant(value='bash', kind=None),
                                            Constant(value='-c', kind=None),
                                            Constant(value='. /home/pi/odoo/addons/point_of_sale/tools/posbox/configuration/upgrade.sh; cleanup', kind=None),
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
                    name='get_six_terminal',
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
                            targets=[Name(id='terminal_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='read_file_first_line',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='odoo-six-payment-terminal.conf', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='terminal_id', ctx=Load()),
                                    Constant(value='Not Configured', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_homepage_data',
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
                            targets=[Name(id='hostname', ctx=Store())],
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='socket', ctx=Load()),
                                            attr='gethostname',
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
                            targets=[Name(id='wired', ctx=Store())],
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
                                                            Constant(value='cat', kind=None),
                                                            Constant(value='/sys/class/net/eth0/operstate', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='wired', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='up', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='network', ctx=Store())],
                                    value=Constant(value='Ethernet', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='ssid', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='access_point',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='network', ctx=Store())],
                                                    value=Constant(value='Wifi access point', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='network', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='Wifi : ', kind=None),
                                                        op=Add(),
                                                        right=Name(id='ssid', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='network', ctx=Store())],
                                            value=Constant(value='Not Connected', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='iot_device', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='device', ctx=Store()),
                            iter=Name(id='iot_devices', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='iot_device', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='identifier', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='iot_devices', ctx=Load()),
                                                                    slice=Name(id='device', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='device_name',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value=' : ', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='iot_devices', ctx=Load()),
                                                                            slice=Name(id='device', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='data',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='value', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='iot_devices', ctx=Load()),
                                                                    slice=Name(id='device', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='device_type',
                                                                ctx=Load(),
                                                            ),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='_', kind=None),
                                                            Constant(value=' ', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='iot_devices', ctx=Load()),
                                                            slice=Name(id='device', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='device_identifier',
                                                        ctx=Load(),
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='hostname', kind=None),
                                    Constant(value='ip', kind=None),
                                    Constant(value='mac', kind=None),
                                    Constant(value='iot_device_status', kind=None),
                                    Constant(value='server_status', kind=None),
                                    Constant(value='six_terminal', kind=None),
                                    Constant(value='network_status', kind=None),
                                    Constant(value='version', kind=None),
                                ],
                                values=[
                                    Name(id='hostname', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
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
                                    Name(id='iot_device', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='get_odoo_server_url',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='Not Configured', kind=None),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_six_terminal',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='network', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_version',
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
                    name='index',
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
                            targets=[Name(id='wifi', ctx=Store())],
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
                                right=Constant(value='wifi_network.txt', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remote_server', ctx=Store())],
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
                                right=Constant(value='odoo-remote-server.conf', kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='wifi', ctx=Load()),
                                                        attr='exists',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='remote_server', ctx=Load()),
                                                        attr='exists',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='access_point',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=BinOp(
                                            left=Constant(value="<meta http-equiv='refresh' content='0; url=http://", kind=None),
                                            op=Add(),
                                            right=Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='get_ip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Constant(value=":8069/steps'>", kind=None),
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='homepage_template', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_homepage_data',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/', kind=None)],
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
                FunctionDef(
                    name='list_handlers',
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
                            targets=[Name(id='drivers_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='driver', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='listdir',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='get_resource_path', ctx=Load()),
                                        args=[
                                            Constant(value='hw_drivers', kind=None),
                                            Constant(value='iot_handlers/drivers', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='driver', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='__pycache__', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='drivers_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='driver', ctx=Load())],
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
                        Assign(
                            targets=[Name(id='interfaces_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='interface', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='listdir',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='get_resource_path', ctx=Load()),
                                        args=[
                                            Constant(value='hw_drivers', kind=None),
                                            Constant(value='iot_handlers/interfaces', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='interface', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='__pycache__', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='interfaces_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='interface', ctx=Load())],
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='handler_list_template', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='breadcrumb', kind=None),
                                            Constant(value='drivers_list', kind=None),
                                            Constant(value='interfaces_list', kind=None),
                                            Constant(value='server', kind=None),
                                        ],
                                        values=[
                                            Constant(value="Odoo's IoT Box - Handlers list", kind=None),
                                            Constant(value='Handlers list', kind=None),
                                            Name(id='drivers_list', ctx=Load()),
                                            Name(id='interfaces_list', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='get_odoo_server_url',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
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
                            args=[Constant(value='/list_handlers', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='load_iot_handlers',
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
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='download_iot_handlers',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=False, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='sudo', kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='odoo', kind=None),
                                            Constant(value='restart', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value="<meta http-equiv='refresh' content='20; url=http://", kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=":8069/list_handlers'>", kind=None),
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
                            args=[Constant(value='/load_iot_handlers', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='list_credential',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='list_credential_template', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='breadcrumb', kind=None),
                                            Constant(value='db_uuid', kind=None),
                                            Constant(value='enterprise_code', kind=None),
                                        ],
                                        values=[
                                            Constant(value="Odoo's IoT Box - List credential", kind=None),
                                            Constant(value='List credential', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='read_file_first_line',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='odoo-db-uuid.conf', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='read_file_first_line',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='odoo-enterprise-code.conf', kind=None)],
                                                keywords=[],
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
                            args=[Constant(value='/list_credential', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_credential',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='db_uuid', annotation=None, type_comment=None),
                            arg(arg='enterprise_code', annotation=None, type_comment=None),
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
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='add_credential',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='db_uuid', ctx=Load()),
                                    Name(id='enterprise_code', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='sudo', kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='odoo', kind=None),
                                            Constant(value='restart', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value="<meta http-equiv='refresh' content='20; url=http://", kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=":8069'>", kind=None),
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
                            args=[Constant(value='/save_credential', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear_credential',
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
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='unlink_file',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='odoo-db-uuid.conf', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='unlink_file',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='odoo-enterprise-code.conf', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='sudo', kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='odoo', kind=None),
                                            Constant(value='restart', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value="<meta http-equiv='refresh' content='20; url=http://", kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=":8069'>", kind=None),
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
                            args=[Constant(value='/clear_credential', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='wifi',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='wifi_config_template', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='breadcrumb', kind=None),
                                            Constant(value='loading_message', kind=None),
                                            Constant(value='ssid', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Wifi configuration', kind=None),
                                            Constant(value='Configure Wifi', kind=None),
                                            Constant(value='Connecting to Wifi', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='get_wifi_essid',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
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
                            args=[Constant(value='/wifi', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='connect_to_wifi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='essid', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='persistent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        If(
                            test=Name(id='persistent', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='persistent', ctx=Store())],
                                    value=Constant(value='1', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='persistent', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='get_resource_path', ctx=Load()),
                                                args=[
                                                    Constant(value='point_of_sale', kind=None),
                                                    Constant(value='tools/posbox/configuration/connect_to_wifi.sh', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='essid', ctx=Load()),
                                            Name(id='password', ctx=Load()),
                                            Name(id='persistent', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
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
                        Assign(
                            targets=[Name(id='res_payload', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='message', kind=None)],
                                values=[
                                    BinOp(
                                        left=Constant(value='Connecting to ', kind=None),
                                        op=Add(),
                                        right=Name(id='essid', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='server', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res_payload', ctx=Load()),
                                            slice=Constant(value='server', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='url', kind=None),
                                            Constant(value='message', kind=None),
                                        ],
                                        values=[
                                            Name(id='server', ctx=Load()),
                                            Constant(value='Redirect to Odoo Server', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res_payload', ctx=Load()),
                                            slice=Constant(value='server', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='url', kind=None),
                                            Constant(value='message', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value='http://', kind=None),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Attribute(
                                                            value=Name(id='helpers', ctx=Load()),
                                                            attr='get_ip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value=':8069', kind=None),
                                            ),
                                            Constant(value='Redirect to IoT Box', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[Name(id='res_payload', ctx=Load())],
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
                            args=[Constant(value='/wifi_connect', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear_wifi_configuration',
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
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='unlink_file',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='wifi_network.txt', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value="<meta http-equiv='refresh' content='0; url=http://", kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=":8069'>", kind=None),
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
                            args=[Constant(value='/wifi_clear', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear_server_configuration',
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
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='unlink_file',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='odoo-remote-server.conf', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value="<meta http-equiv='refresh' content='0; url=http://", kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=":8069'>", kind=None),
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
                            args=[Constant(value='/server_clear', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear_handlers_list',
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
                        For(
                            target=Name(id='directory', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='drivers', kind=None),
                                    Constant(value='interfaces', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                For(
                                    target=Name(id='file', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='listdir',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='get_resource_path', ctx=Load()),
                                                args=[
                                                    Constant(value='hw_drivers', kind=None),
                                                    Constant(value='iot_handlers', kind=None),
                                                    Name(id='directory', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='file', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='__pycache__', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='helpers', ctx=Load()),
                                                            attr='unlink_file',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='get_resource_path', ctx=Load()),
                                                                args=[
                                                                    Constant(value='hw_drivers', kind=None),
                                                                    Constant(value='iot_handlers', kind=None),
                                                                    Name(id='directory', ctx=Load()),
                                                                    Name(id='file', ctx=Load()),
                                                                ],
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
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value="<meta http-equiv='refresh' content='0; url=http://", kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=":8069/list_handlers'>", kind=None),
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
                            args=[Constant(value='/handlers_clear', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='connect_to_server',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='iotname', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Name(id='token', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='credential', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='token', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='|', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='credential', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='credential', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='credential', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='db_uuid', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='credential', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='enterprise_code', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='credential', ctx=Load()),
                                                slice=Constant(value=3, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='add_credential',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='db_uuid', ctx=Load()),
                                                    Name(id='enterprise_code', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
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
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_token',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='reboot', ctx=Store())],
                            value=Constant(value='reboot', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='get_resource_path', ctx=Load()),
                                                args=[
                                                    Constant(value='point_of_sale', kind=None),
                                                    Constant(value='tools/posbox/configuration/connect_to_server.sh', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='url', ctx=Load()),
                                            Name(id='iotname', ctx=Load()),
                                            Name(id='token', ctx=Load()),
                                            Name(id='reboot', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value='http://', kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=':8069', kind=None),
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
                            args=[Constant(value='/server_connect', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='step_by_step_configure_page',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='configure_wizard_template', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='breadcrumb', kind=None),
                                            Constant(value='loading_message', kind=None),
                                            Constant(value='ssid', kind=None),
                                            Constant(value='server', kind=None),
                                            Constant(value='hostname', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Configure IoT Box', kind=None),
                                            Constant(value='Configure IoT Box', kind=None),
                                            Constant(value='Configuring your IoT Box', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='get_wifi_essid',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='helpers', ctx=Load()),
                                                            attr='get_odoo_server_url',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='subprocess', ctx=Load()),
                                                                    attr='check_output',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='hostname', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='utf-8', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='\n', kind=None)],
                                                keywords=[],
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
                            args=[Constant(value='/steps', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='step_by_step_configure',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='iotname', annotation=None, type_comment=None),
                            arg(arg='essid', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='persistent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        If(
                            test=Name(id='token', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='token', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='|', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='token', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='token', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='|', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='get_resource_path', ctx=Load()),
                                                args=[
                                                    Constant(value='point_of_sale', kind=None),
                                                    Constant(value='tools/posbox/configuration/connect_to_server_wifi.sh', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='url', ctx=Load()),
                                            Name(id='iotname', ctx=Load()),
                                            Name(id='token', ctx=Load()),
                                            Name(id='essid', ctx=Load()),
                                            Name(id='password', ctx=Load()),
                                            Name(id='persistent', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='url', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/step_configure', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='server',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='server_config_template', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='breadcrumb', kind=None),
                                            Constant(value='hostname', kind=None),
                                            Constant(value='server_status', kind=None),
                                            Constant(value='loading_message', kind=None),
                                        ],
                                        values=[
                                            Constant(value='IoT -> Odoo server configuration', kind=None),
                                            Constant(value='Configure Odoo Server', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='subprocess', ctx=Load()),
                                                                    attr='check_output',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='hostname', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='utf-8', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='\n', kind=None)],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='helpers', ctx=Load()),
                                                            attr='get_odoo_server_url',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='Not configured yet', kind=None),
                                                ],
                                            ),
                                            Constant(value='Configure Domain Server', kind=None),
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
                            args=[Constant(value='/server', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='remote_connect',
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
                            value=Constant(value='\n        Establish a link with a customer box trough internet with a ssh tunnel\n        1 - take a new auth_token on https://dashboard.ngrok.com/\n        2 - copy past this auth_token on the IoT Box : http://IoT_Box:8069/remote_connect\n        3 - check on ngrok the port and url to get access to the box\n        4 - you can connect to the box with this command : ssh -p port -v pi@url\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='remote_connect_template', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='breadcrumb', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Remote debugging', kind=None),
                                            Constant(value='Remote Debugging', kind=None),
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
                            args=[Constant(value='/remote_connect', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
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
                    name='enable_ngrok',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='auth_token', annotation=None, type_comment=None),
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
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='subprocess', ctx=Load()),
                                        attr='call',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Constant(value='pgrep', kind=None),
                                                Constant(value='ngrok', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
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
                                                    Constant(value='ngrok', kind=None),
                                                    Constant(value='tcp', kind=None),
                                                    Constant(value='-authtoken', kind=None),
                                                    Name(id='auth_token', ctx=Load()),
                                                    Constant(value='-log', kind=None),
                                                    Constant(value='/tmp/ngrok.log', kind=None),
                                                    Constant(value='22', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=BinOp(
                                        left=Constant(value='starting with ', kind=None),
                                        op=Add(),
                                        right=Name(id='auth_token', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Constant(value='already running', kind=None),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/enable_ngrok', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='six_payment_terminal',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='six_payment_terminal_template', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='breadcrumb', kind=None),
                                            Constant(value='terminalId', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Six Payment Terminal', kind=None),
                                            Constant(value='Six Payment Terminal', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_six_terminal',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
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
                            args=[Constant(value='/six_payment_terminal', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_six_payment_terminal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='terminal_id', annotation=None, type_comment=None),
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
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='write_file',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='odoo-six-payment-terminal.conf', kind=None),
                                    Name(id='terminal_id', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='sudo', kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='odoo', kind=None),
                                            Constant(value='restart', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value='http://', kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=':8069', kind=None),
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
                            args=[Constant(value='/six_payment_terminal_add', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear_six_payment_terminal',
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
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='unlink_file',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='odoo-six-payment-terminal.conf', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='sudo', kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='odoo', kind=None),
                                            Constant(value='restart', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value="<meta http-equiv='refresh' content='0; url=http://", kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='get_ip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=":8069'>", kind=None),
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
                            args=[Constant(value='/six_payment_terminal_clear', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='upgrade',
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
                            targets=[Name(id='commit', ctx=Store())],
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
                                                            Constant(value='git', kind=None),
                                                            Constant(value='--work-tree=/home/pi/odoo/', kind=None),
                                                            Constant(value='--git-dir=/home/pi/odoo/.git', kind=None),
                                                            Constant(value='log', kind=None),
                                                            Constant(value='-1', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\n', kind=None),
                                    Constant(value='<br/>', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='flashToVersion', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='check_image',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='actualVersion', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='get_version',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='flashToVersion', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='flashToVersion', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='flashToVersion', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='major', kind=None),
                                                        Constant(value='', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='flashToVersion', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='minor', kind=None),
                                                        Constant(value='', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='upgrade_page_template', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='breadcrumb', kind=None),
                                            Constant(value='loading_message', kind=None),
                                            Constant(value='commit', kind=None),
                                            Constant(value='flashToVersion', kind=None),
                                            Constant(value='actualVersion', kind=None),
                                        ],
                                        values=[
                                            Constant(value="Odoo's IoTBox - Software Upgrade", kind=None),
                                            Constant(value='IoT Box Software Upgrade', kind=None),
                                            Constant(value='Updating IoT box', kind=None),
                                            Name(id='commit', ctx=Load()),
                                            Name(id='flashToVersion', ctx=Load()),
                                            Name(id='actualVersion', ctx=Load()),
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
                            args=[Constant(value='/hw_proxy/upgrade', kind=None)],
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
                FunctionDef(
                    name='perform_upgrade',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='updating',
                                        ctx=Load(),
                                    ),
                                    attr='acquire',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='system',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/home/pi/odoo/addons/point_of_sale/tools/posbox/configuration/posbox_update.sh', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='updating',
                                        ctx=Load(),
                                    ),
                                    attr='release',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Constant(value='SUCCESS', kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/hw_proxy/perform_upgrade', kind=None)],
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
                FunctionDef(
                    name='check_version',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='get_version',
                                    ctx=Load(),
                                ),
                                args=[],
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
                            args=[Constant(value='/hw_proxy/get_version', kind=None)],
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
                FunctionDef(
                    name='perform_flashing_create_partition',
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
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Subscript(
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
                                                                        Constant(value='sudo', kind=None),
                                                                        Constant(value='bash', kind=None),
                                                                        Constant(value='-c', kind=None),
                                                                        Constant(value='. /home/pi/odoo/addons/point_of_sale/tools/posbox/configuration/upgrade.sh; create_partition', kind=None),
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
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='\n', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=2, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='response', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='Error_Card_Size', kind=None),
                                                    Constant(value='Error_Upgrade_Already_Started', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[Name(id='response', ctx=Load())],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='Response', ctx=Load()),
                                        args=[Constant(value='success', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='status',
                                                value=Constant(value=200, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='subprocess', ctx=Load()),
                                        attr='CalledProcessError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='output',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
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
                                        Return(
                                            value=Call(
                                                func=Name(id='Response', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='status',
                                                        value=Constant(value=500, kind=None),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/hw_proxy/perform_flashing_create_partition', kind=None)],
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
                FunctionDef(
                    name='perform_flashing_download_raspios',
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
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Subscript(
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
                                                                        Constant(value='sudo', kind=None),
                                                                        Constant(value='bash', kind=None),
                                                                        Constant(value='-c', kind=None),
                                                                        Constant(value='. /home/pi/odoo/addons/point_of_sale/tools/posbox/configuration/upgrade.sh; download_raspios', kind=None),
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
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='\n', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=2, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='response', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='Error_Raspios_Download', kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[Name(id='response', ctx=Load())],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='Response', ctx=Load()),
                                        args=[Constant(value='success', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='status',
                                                value=Constant(value=200, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='subprocess', ctx=Load()),
                                        attr='CalledProcessError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='output',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
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
                                                    attr='clean_partition',
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
                                        Return(
                                            value=Call(
                                                func=Name(id='Response', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='status',
                                                        value=Constant(value=500, kind=None),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/hw_proxy/perform_flashing_download_raspios', kind=None)],
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
                FunctionDef(
                    name='perform_flashing_copy_raspios',
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
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Subscript(
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
                                                                        Constant(value='sudo', kind=None),
                                                                        Constant(value='bash', kind=None),
                                                                        Constant(value='-c', kind=None),
                                                                        Constant(value='. /home/pi/odoo/addons/point_of_sale/tools/posbox/configuration/upgrade.sh; copy_raspios', kind=None),
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
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='\n', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=2, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='response', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='Error_Iotbox_Download', kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[Name(id='response', ctx=Load())],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='Response', ctx=Load()),
                                        args=[Constant(value='success', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='status',
                                                value=Constant(value=200, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='subprocess', ctx=Load()),
                                        attr='CalledProcessError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='output',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
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
                                                    attr='clean_partition',
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
                                        Return(
                                            value=Call(
                                                func=Name(id='Response', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='status',
                                                        value=Constant(value=500, kind=None),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/hw_proxy/perform_flashing_copy_raspios', kind=None)],
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
