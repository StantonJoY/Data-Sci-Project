Module(
    body=[
        ImportFrom(
            module='base64',
            names=[alias(name='b64decode', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='send_file', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_resource_path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.event_manager',
            names=[alias(name='event_manager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.main',
            names=[
                alias(name='iot_devices', asname=None),
                alias(name='manager', asname=None),
            ],
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
        ClassDef(
            name='DriverController',
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
                    name='action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='session_id', annotation=None, type_comment=None),
                            arg(arg='device_identifier', annotation=None, type_comment=None),
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
                            value=Constant(value='\n        This route is called when we want to make a action with device (take picture, printing,...)\n        We specify in data from which session_id that action is called\n        And call the action of specific device\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='iot_device', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='iot_devices', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='device_identifier', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='iot_device', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='iot_device', ctx=Load()),
                                                attr='data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='owner', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='session_id', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='loads',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='iot_device', ctx=Load()),
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
                            args=[Constant(value='/hw_drivers/action', kind=None)],
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
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_certificate',
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
                            value=Constant(value='\n        This route is called when we want to check if certificate is up-to-date\n        Used in cron.daily\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='check_certificate',
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
                            args=[Constant(value='/hw_drivers/check_certificate', kind=None)],
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
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='event',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='listener', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        listener is a dict in witch there are a sessions_id and a dict of device_identifier to listen\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='req', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event_manager', ctx=Load()),
                                    attr='add_request',
                                    ctx=Load(),
                                ),
                                args=[Name(id='listener', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='oldest_time', ctx=Store())],
                            value=BinOp(
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
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='event', ctx=Store()),
                            iter=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='event_manager', ctx=Load()),
                                        attr='events',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='event', ctx=Load()),
                                            slice=Constant(value='time', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[Name(id='oldest_time', ctx=Load())],
                                    ),
                                    body=[
                                        Delete(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='event_manager', ctx=Load()),
                                                        attr='events',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Del(),
                                                ),
                                            ],
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='event', ctx=Load()),
                                                    slice=Constant(value='device_identifier', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='listener', ctx=Load()),
                                                        slice=Constant(value='devices', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='event', ctx=Load()),
                                                    slice=Constant(value='time', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='listener', ctx=Load()),
                                                        slice=Constant(value='last_event', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='event', ctx=Load()),
                                                    slice=Constant(value='session_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='req', ctx=Load()),
                                                slice=Constant(value='session_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Name(id='event', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='req', ctx=Load()),
                                        slice=Constant(value='event', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='wait',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=50, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='req', ctx=Load()),
                                                slice=Constant(value='event', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='clear',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='req', ctx=Load()),
                                                slice=Constant(value='result', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='session_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='req', ctx=Load()),
                                        slice=Constant(value='session_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='req', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
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
                            args=[Constant(value='/hw_drivers/event', kind=None)],
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
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='connect_box',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        This route is called when we want that a IoT Box will be connected to a Odoo DB\n        token is a base 64 encoded string and have 2 argument separate by |\n        1 - url of odoo DB\n        2 - token. This token will be compared to the token of Odoo. He have 1 hour lifetime\n        ', kind=None),
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
                            targets=[Name(id='image', ctx=Store())],
                            value=Call(
                                func=Name(id='get_resource_path', ctx=Load()),
                                args=[
                                    Constant(value='hw_drivers', kind=None),
                                    Constant(value='static/img', kind=None),
                                    Constant(value='False.jpg', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='server', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='credential', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='b64decode', ctx=Load()),
                                                        args=[Name(id='token', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
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
                                Try(
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
                                                            Call(
                                                                func=Name(id='get_resource_path', ctx=Load()),
                                                                args=[
                                                                    Constant(value='point_of_sale', kind=None),
                                                                    Constant(value='tools/posbox/configuration/connect_to_server.sh', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Name(id='url', ctx=Load()),
                                                            Constant(value='', kind=None),
                                                            Name(id='token', ctx=Load()),
                                                            Constant(value='noreboot', kind=None),
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
                                                    value=Name(id='manager', ctx=Load()),
                                                    attr='send_alldevices',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='image', ctx=Store())],
                                            value=Call(
                                                func=Name(id='get_resource_path', ctx=Load()),
                                                args=[
                                                    Constant(value='hw_drivers', kind=None),
                                                    Constant(value='static/img', kind=None),
                                                    Constant(value='True.jpg', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='odoo_restart',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=3, kind=None)],
                                                keywords=[],
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
                                                                right=Attribute(
                                                                    value=Name(id='e', ctx=Load()),
                                                                    attr='output',
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
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='isfile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='open', ctx=Load()),
                                                args=[
                                                    Name(id='image', ctx=Load()),
                                                    Constant(value='rb', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='f', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
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
                            args=[Constant(value='/hw_drivers/box/connect', kind=None)],
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
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='download_logs',
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
                            value=Constant(value='\n        Downloads the log file\n        ', kind=None),
                        ),
                        If(
                            test=Subscript(
                                value=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='logfile', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Name(id='send_file', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='config',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='logfile', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='mimetype',
                                                value=Constant(value='text/plain', kind=None),
                                            ),
                                            keyword(
                                                arg='as_attachment',
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
                                                value=Name(id='res', ctx=Load()),
                                                attr='headers',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='Cache-Control', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='no-cache', kind=None),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='res', ctx=Load()),
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
                            args=[Constant(value='/hw_drivers/download_logs', kind=None)],
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
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
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
