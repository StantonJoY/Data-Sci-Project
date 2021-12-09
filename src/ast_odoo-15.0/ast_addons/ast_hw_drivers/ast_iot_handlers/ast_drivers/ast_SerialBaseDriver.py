Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='namedtuple', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='contextlib',
            names=[alias(name='contextmanager', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='serial', asname=None)],
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
            names=[alias(name='traceback', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.event_manager',
            names=[alias(name='event_manager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.driver',
            names=[alias(name='Driver', asname=None)],
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
            targets=[Name(id='SerialProtocol', ctx=Store())],
            value=Call(
                func=Name(id='namedtuple', ctx=Load()),
                args=[
                    Constant(value='SerialProtocol', kind=None),
                    Constant(value='name baudrate bytesize stopbits parity timeout writeTimeout measureRegexp statusRegexp commandTerminator commandDelay measureDelay newMeasureDelay measureCommand emptyAnswerValid', kind=None),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='serial_connection',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='path', annotation=None, type_comment=None),
                    arg(arg='protocol', annotation=None, type_comment=None),
                    arg(arg='is_probing', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Opens a serial connection to a device and closes it automatically after use.\n\n    :param path: path to the device\n    :type path: string\n    :param protocol: an object containing the serial protocol to connect to a device\n    :type protocol: namedtuple\n    :param is_probing: a flag thet if set to `True` makes the timeouts longer, defaults to False\n    :type is_probing: bool, optional\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='PROBING_TIMEOUT', ctx=Store())],
                    value=Constant(value=1, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='port_config', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='baudrate', kind=None),
                            Constant(value='bytesize', kind=None),
                            Constant(value='stopbits', kind=None),
                            Constant(value='parity', kind=None),
                            Constant(value='timeout', kind=None),
                            Constant(value='writeTimeout', kind=None),
                        ],
                        values=[
                            Attribute(
                                value=Name(id='protocol', ctx=Load()),
                                attr='baudrate',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='protocol', ctx=Load()),
                                attr='bytesize',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='protocol', ctx=Load()),
                                attr='stopbits',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='protocol', ctx=Load()),
                                attr='parity',
                                ctx=Load(),
                            ),
                            IfExp(
                                test=Name(id='is_probing', ctx=Load()),
                                body=Name(id='PROBING_TIMEOUT', ctx=Load()),
                                orelse=Attribute(
                                    value=Name(id='protocol', ctx=Load()),
                                    attr='timeout',
                                    ctx=Load(),
                                ),
                            ),
                            IfExp(
                                test=Name(id='is_probing', ctx=Load()),
                                body=Name(id='PROBING_TIMEOUT', ctx=Load()),
                                orelse=Attribute(
                                    value=Name(id='protocol', ctx=Load()),
                                    attr='writeTimeout',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='connection', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='serial', ctx=Load()),
                            attr='Serial',
                            ctx=Load(),
                        ),
                        args=[Name(id='path', ctx=Load())],
                        keywords=[
                            keyword(
                                arg=None,
                                value=Name(id='port_config', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Yield(
                        value=Name(id='connection', ctx=Load()),
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='connection', ctx=Load()),
                            attr='close',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[Name(id='contextmanager', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='SerialDriver',
            bases=[Name(id='Driver', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Abstract base class for serial drivers.', kind=None),
                ),
                Assign(
                    targets=[Name(id='_protocol', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='connection_type', ctx=Store())],
                    value=Constant(value='serial', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='STATUS_CONNECTED', ctx=Store())],
                    value=Constant(value='connected', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='STATUS_ERROR', ctx=Store())],
                    value=Constant(value='error', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='STATUS_CONNECTING', ctx=Store())],
                    value=Constant(value='connecting', kind=None),
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
                            value=Constant(value=' Attributes initialization method for `SerialDriver`.\n\n        :param device: path to the device\n        :type device: str\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SerialDriver', ctx=Load()),
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
                                        keys=[Constant(value='get_status', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_push_status',
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
                                    attr='device_connection',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='serial', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_device_lock',
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
                                    attr='_status',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='status', kind=None),
                                    Constant(value='message_title', kind=None),
                                    Constant(value='message_body', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='STATUS_CONNECTING',
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_name',
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
                    name='_get_raw_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='connection', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_push_status',
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
                            value=Constant(value='Updates the current status and pushes it to the frontend.', kind=None),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='status', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_status',
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
                    ],
                    decorator_list=[],
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
                        Expr(
                            value=Constant(value="Tries to build the device's name based on its type and protocol name but falls back on a default name if that doesn't work.", kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Constant(value='%s serial %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_protocol',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='device_type',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='title',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='name', ctx=Store())],
                                            value=Constant(value='Unknown Serial Device', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device_name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='name', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_take_measure',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_do_action',
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
                            value=Constant(value='Helper function that calls a specific action method on the device.\n\n        :param data: the `_actions` key mapped to the action method we want to call\n        :type data: string\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_device_lock',
                                                ctx=Load(),
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_actions',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='action', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='data', ctx=Load())],
                                                keywords=[],
                                            ),
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
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_protocol',
                                                            ctx=Load(),
                                                        ),
                                                        attr='commandDelay',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='An error occured while performing action %s on %s', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='data', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='device_name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_status',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='status', kind=None),
                                                    Constant(value='message_title', kind=None),
                                                    Constant(value='message_body', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='STATUS_ERROR',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='msg', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='traceback', ctx=Load()),
                                                            attr='format_exc',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                                                    attr='_push_status',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    name='action',
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
                            value=Constant(value='Establish a connection with the device if needed and have it perform a specific action.\n\n        :param data: the `_actions` key mapped to the action method we want to call\n        :type data: string\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_connection',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_connection',
                                                ctx=Load(),
                                            ),
                                            attr='isOpen',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_do_action',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='serial_connection', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='device_identifier',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_protocol',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='connection', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_connection',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='connection', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_do_action',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='data', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
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
                        Expr(
                            value=Constant(value='Continuously gets new measures from the device.', kind=None),
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='serial_connection', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='device_identifier',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_protocol',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='connection', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_connection',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='connection', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_status',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='status', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='STATUS_CONNECTED',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_push_status',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        While(
                                            test=UnaryOp(
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
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_take_measure',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
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
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_protocol',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='newMeasureDelay',
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
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Error while reading %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='device_name',
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
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_status',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='status', kind=None),
                                                    Constant(value='message_title', kind=None),
                                                    Constant(value='message_body', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='STATUS_ERROR',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='msg', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='traceback', ctx=Load()),
                                                            attr='format_exc',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                                                    attr='_push_status',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
