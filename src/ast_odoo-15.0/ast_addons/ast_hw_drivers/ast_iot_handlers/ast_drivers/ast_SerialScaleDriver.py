Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='namedtuple', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='serial', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.controllers.proxy',
            names=[alias(name='proxy_drivers', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.event_manager',
            names=[alias(name='event_manager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.iot_handlers.drivers.SerialBaseDriver',
            names=[
                alias(name='SerialDriver', asname=None),
                alias(name='SerialProtocol', asname=None),
                alias(name='serial_connection', asname=None),
            ],
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
            targets=[Name(id='ACTIVE_SCALE', ctx=Store())],
            value=Constant(value=None, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='new_weight_event', ctx=Store())],
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
            targets=[Name(id='ScaleProtocol', ctx=Store())],
            value=Call(
                func=Name(id='namedtuple', ctx=Load()),
                args=[
                    Constant(value='ScaleProtocol', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='SerialProtocol', ctx=Load()),
                            attr='_fields',
                            ctx=Load(),
                        ),
                        op=Add(),
                        right=Tuple(
                            elts=[
                                Constant(value='zeroCommand', kind=None),
                                Constant(value='tareCommand', kind=None),
                                Constant(value='clearCommand', kind=None),
                                Constant(value='autoResetWeight', kind=None),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='Toledo8217Protocol', ctx=Store())],
            value=Call(
                func=Name(id='ScaleProtocol', ctx=Load()),
                args=[],
                keywords=[
                    keyword(
                        arg='name',
                        value=Constant(value='Toledo 8217', kind=None),
                    ),
                    keyword(
                        arg='baudrate',
                        value=Constant(value=9600, kind=None),
                    ),
                    keyword(
                        arg='bytesize',
                        value=Attribute(
                            value=Name(id='serial', ctx=Load()),
                            attr='SEVENBITS',
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
                        arg='parity',
                        value=Attribute(
                            value=Name(id='serial', ctx=Load()),
                            attr='PARITY_EVEN',
                            ctx=Load(),
                        ),
                    ),
                    keyword(
                        arg='timeout',
                        value=Constant(value=1, kind=None),
                    ),
                    keyword(
                        arg='writeTimeout',
                        value=Constant(value=1, kind=None),
                    ),
                    keyword(
                        arg='measureRegexp',
                        value=Constant(value=b'\x02\\s*([0-9.]+)N?\\r', kind=None),
                    ),
                    keyword(
                        arg='statusRegexp',
                        value=Constant(value=b'\x02\\s*(\\?.)\\r', kind=None),
                    ),
                    keyword(
                        arg='commandDelay',
                        value=Constant(value=0.2, kind=None),
                    ),
                    keyword(
                        arg='measureDelay',
                        value=Constant(value=0.5, kind=None),
                    ),
                    keyword(
                        arg='newMeasureDelay',
                        value=Constant(value=0.2, kind=None),
                    ),
                    keyword(
                        arg='commandTerminator',
                        value=Constant(value=b'', kind=None),
                    ),
                    keyword(
                        arg='measureCommand',
                        value=Constant(value=b'W', kind=None),
                    ),
                    keyword(
                        arg='zeroCommand',
                        value=Constant(value=b'Z', kind=None),
                    ),
                    keyword(
                        arg='tareCommand',
                        value=Constant(value=b'T', kind=None),
                    ),
                    keyword(
                        arg='clearCommand',
                        value=Constant(value=b'C', kind=None),
                    ),
                    keyword(
                        arg='emptyAnswerValid',
                        value=Constant(value=False, kind=None),
                    ),
                    keyword(
                        arg='autoResetWeight',
                        value=Constant(value=False, kind=None),
                    ),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='ADAMEquipmentProtocol', ctx=Store())],
            value=Call(
                func=Name(id='ScaleProtocol', ctx=Load()),
                args=[],
                keywords=[
                    keyword(
                        arg='name',
                        value=Constant(value='Adam Equipment', kind=None),
                    ),
                    keyword(
                        arg='baudrate',
                        value=Constant(value=4800, kind=None),
                    ),
                    keyword(
                        arg='bytesize',
                        value=Attribute(
                            value=Name(id='serial', ctx=Load()),
                            attr='EIGHTBITS',
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
                        arg='parity',
                        value=Attribute(
                            value=Name(id='serial', ctx=Load()),
                            attr='PARITY_NONE',
                            ctx=Load(),
                        ),
                    ),
                    keyword(
                        arg='timeout',
                        value=Constant(value=0.2, kind=None),
                    ),
                    keyword(
                        arg='writeTimeout',
                        value=Constant(value=0.2, kind=None),
                    ),
                    keyword(
                        arg='measureRegexp',
                        value=Constant(value=b'\\s*([0-9.]+)kg', kind=None),
                    ),
                    keyword(
                        arg='statusRegexp',
                        value=Constant(value=None, kind=None),
                    ),
                    keyword(
                        arg='commandTerminator',
                        value=Constant(value=b'\r\n', kind=None),
                    ),
                    keyword(
                        arg='commandDelay',
                        value=Constant(value=0.2, kind=None),
                    ),
                    keyword(
                        arg='measureDelay',
                        value=Constant(value=0.5, kind=None),
                    ),
                    keyword(
                        arg='newMeasureDelay',
                        value=Constant(value=5, kind=None),
                    ),
                    keyword(
                        arg='measureCommand',
                        value=Constant(value=b'P', kind=None),
                    ),
                    keyword(
                        arg='zeroCommand',
                        value=Constant(value=b'Z', kind=None),
                    ),
                    keyword(
                        arg='tareCommand',
                        value=Constant(value=b'T', kind=None),
                    ),
                    keyword(
                        arg='clearCommand',
                        value=Constant(value=None, kind=None),
                    ),
                    keyword(
                        arg='emptyAnswerValid',
                        value=Constant(value=True, kind=None),
                    ),
                    keyword(
                        arg='autoResetWeight',
                        value=Constant(value=True, kind=None),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ScaleReadOldRoute',
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
                    name='scale_read',
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
                            test=Name(id='ACTIVE_SCALE', ctx=Load()),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='weight', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ACTIVE_SCALE', ctx=Load()),
                                                    attr='_scale_read_old_route',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
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
                            args=[Constant(value='/hw_proxy/scale_read', kind=None)],
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
        ClassDef(
            name='ScaleDriver',
            bases=[Name(id='SerialDriver', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Abstract base class for scale drivers.', kind=None),
                ),
                Assign(
                    targets=[Name(id='last_sent_value', ctx=Store())],
                    value=Constant(value=None, kind=None),
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
                                            Name(id='ScaleDriver', ctx=Load()),
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
                            value=Constant(value='scale', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_actions',
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
                                    attr='_is_reading',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Global(names=['ACTIVE_SCALE']),
                        Assign(
                            targets=[Name(id='ACTIVE_SCALE', ctx=Store())],
                            value=Name(id='self', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='proxy_drivers', ctx=Load()),
                                    slice=Constant(value='scale', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='ACTIVE_SCALE', ctx=Load()),
                            type_comment=None,
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
                            value=Constant(value='Allows `hw_proxy.Proxy` to retrieve the status of the scales', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='status', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_status',
                                ctx=Load(),
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
                                    Subscript(
                                        value=Name(id='status', ctx=Load()),
                                        slice=Constant(value='status', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Subscript(
                                                value=Name(id='status', ctx=Load()),
                                                slice=Constant(value='message_title', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
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
                    name='_set_actions',
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
                            value=Constant(value='Initializes `self._actions`, a map of action keys sent by the frontend to backend action methods.', kind=None),
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
                                            Constant(value='read_once', kind=None),
                                            Constant(value='set_zero', kind=None),
                                            Constant(value='set_tare', kind=None),
                                            Constant(value='clear_tare', kind=None),
                                            Constant(value='start_reading', kind=None),
                                            Constant(value='stop_reading', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_read_once_action',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_set_zero_action',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_set_tare_action',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_clear_tare_action',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_start_reading_action',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_stop_reading_action',
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
                    name='_start_reading_action',
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
                            value=Constant(value='Starts asking for the scale value.', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_reading',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_stop_reading_action',
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
                            value=Constant(value='Stops asking for the scale value.', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_reading',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_clear_tare_action',
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
                            value=Constant(value='Clears the scale current tare weight.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='clearCommand', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_protocol',
                                            ctx=Load(),
                                        ),
                                        attr='clearCommand',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_protocol',
                                            ctx=Load(),
                                        ),
                                        attr='tareCommand',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_connection',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='clearCommand', ctx=Load()),
                                        op=Add(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_protocol',
                                                ctx=Load(),
                                            ),
                                            attr='commandTerminator',
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
                    name='_read_once_action',
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
                            value=Constant(value='Reads the scale current weight value and pushes it to the frontend.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_read_weight',
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
                                    attr='last_sent_value',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='value', kind=None),
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
                    name='_set_zero_action',
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
                            value=Constant(value='Makes the weight currently applied to the scale the new zero.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_connection',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_protocol',
                                                ctx=Load(),
                                            ),
                                            attr='zeroCommand',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_protocol',
                                                ctx=Load(),
                                            ),
                                            attr='commandTerminator',
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
                    name='_set_tare_action',
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
                            value=Constant(value="Sets the scale's current weight value as tare weight.", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_connection',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_protocol',
                                                ctx=Load(),
                                            ),
                                            attr='tareCommand',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_protocol',
                                                ctx=Load(),
                                            ),
                                            attr='commandTerminator',
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
                    body=[
                        Expr(
                            value=Constant(value="Gets raw bytes containing the updated value of the device.\n\n        :param connection: a connection to the device's serial port\n        :type connection: pyserial.Serial\n        :return: the raw response to a weight request\n        :rtype: str\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='answer', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=Constant(value=True, kind=None),
                            body=[
                                Assign(
                                    targets=[Name(id='char', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='connection', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=1, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='char', ctx=Load()),
                                    ),
                                    body=[Break()],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='answer', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='bytes', ctx=Load()),
                                                        args=[Name(id='char', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=b'', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='answer', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='staticmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_read_weight',
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
                            value=Constant(value='Asks for a new weight from the scale, checks if it is valid and, if it is, makes it the current value.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='protocol', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_protocol',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_connection',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='protocol', ctx=Load()),
                                            attr='measureCommand',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='protocol', ctx=Load()),
                                            attr='commandTerminator',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='answer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_raw_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_connection',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_protocol',
                                            ctx=Load(),
                                        ),
                                        attr='measureRegexp',
                                        ctx=Load(),
                                    ),
                                    Name(id='answer', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='match', ctx=Load()),
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
                                            Constant(value='status', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='float', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='match', ctx=Load()),
                                                            attr='group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=1, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_status',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                    name='_scale_read_old_route',
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
                            value=Constant(value='Used when the iot app is not installed', kind=None),
                        ),
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_read_weight',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='value', kind=None),
                                ctx=Load(),
                            ),
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
                    body=[
                        Expr(
                            value=Constant(value="Reads the device's weight value, and pushes that value to the frontend.", kind=None),
                        ),
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_read_weight',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='last_sent_value',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_status',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='status', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='STATUS_ERROR',
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
                                                    attr='last_sent_value',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='value', kind=None),
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Toledo8217Driver',
            bases=[Name(id='ScaleDriver', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Driver for the Toldedo 8217 serial scale.', kind=None),
                ),
                Assign(
                    targets=[Name(id='_protocol', ctx=Store())],
                    value=Name(id='Toledo8217Protocol', ctx=Load()),
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
                                            Name(id='Toledo8217Driver', ctx=Load()),
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
                                    attr='device_manufacturer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Toledo', kind=None),
                            type_comment=None,
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
                        Expr(
                            value=Constant(value='Checks whether the device, which port info is passed as argument, is supported by the driver.\n\n        :param device: path to the device\n        :type device: str\n        :return: whether the device is supported by the driver\n        :rtype: bool\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='protocol', ctx=Store())],
                            value=Attribute(
                                value=Name(id='cls', ctx=Load()),
                                attr='_protocol',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='serial_connection', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='device', ctx=Load()),
                                                        slice=Constant(value='identifier', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='protocol', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='is_probing',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=Name(id='connection', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='connection', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value=b'Ehello', kind=None),
                                                        op=Add(),
                                                        right=Attribute(
                                                            value=Name(id='protocol', ctx=Load()),
                                                            attr='commandTerminator',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                                        value=Name(id='protocol', ctx=Load()),
                                                        attr='commandDelay',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='answer', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='connection', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=8, kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='answer', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value=b'\x02E\rhello', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='connection', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value=b'F', kind=None),
                                                                op=Add(),
                                                                right=Attribute(
                                                                    value=Name(id='protocol', ctx=Load()),
                                                                    attr='commandTerminator',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Return(
                                                    value=Constant(value=True, kind=None),
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
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='serial', ctx=Load()),
                                            attr='serialutil',
                                            ctx=Load(),
                                        ),
                                        attr='SerialTimeoutException',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Pass()],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Error while probing %s with protocol %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='device', ctx=Load()),
                                                                Attribute(
                                                                    value=Name(id='protocol', ctx=Load()),
                                                                    attr='name',
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
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AdamEquipmentDriver',
            bases=[Name(id='ScaleDriver', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Driver for the Adam Equipment serial scale.', kind=None),
                ),
                Assign(
                    targets=[Name(id='_protocol', ctx=Store())],
                    value=Name(id='ADAMEquipmentProtocol', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='priority', ctx=Store())],
                    value=Constant(value=0, kind=None),
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
                                            Name(id='AdamEquipmentDriver', ctx=Load()),
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
                                    attr='_is_reading',
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
                                    attr='_last_weight_time',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='device_manufacturer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Adam', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_last_weight_time',
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
                            value=Constant(value='The ADAM doesn\'t make the difference between a value of 0 and "the same value as last time":\n        in both cases it returns an empty string.\n        With this, unless the weight changes, we give the user `TIME_WEIGHT_KEPT` seconds to log the new weight,\n        then change it back to zero to avoid keeping it indefinetely, which could cause issues.\n        In any case the ADAM must always go back to zero before it can weight again.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='TIME_WEIGHT_KEPT', ctx=Store())],
                            value=Constant(value=10, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='value', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=BinOp(
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
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_last_weight_time',
                                                ctx=Load(),
                                            ),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Name(id='TIME_WEIGHT_KEPT', ctx=Load())],
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
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
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
                                            attr='_last_weight_time',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='time',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                    body=[
                        Expr(
                            value=Constant(value="Reads the device's weight value, and pushes that value to the frontend.", kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_is_reading',
                                ctx=Load(),
                            ),
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
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_read_weight',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_check_last_weight_time',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='value', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='last_sent_value',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_status',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='status', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='STATUS_ERROR',
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
                                                            attr='last_sent_value',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='value', kind=None),
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
                                            orelse=[],
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='sleep',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0.5, kind=None)],
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
                    name='_scale_read_old_route',
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
                            value=Constant(value='Used when the iot app is not installed', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='sleep',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=3, kind=None)],
                                keywords=[],
                            ),
                        ),
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_read_weight',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_last_weight_time',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='value', kind=None),
                                ctx=Load(),
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
                        Expr(
                            value=Constant(value='Checks whether the device at `device` is supported by the driver.\n\n        :param device: path to the device\n        :type device: str\n        :return: whether the device is supported by the driver\n        :rtype: bool\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='protocol', ctx=Store())],
                            value=Attribute(
                                value=Name(id='cls', ctx=Load()),
                                attr='_protocol',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='serial_connection', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='device', ctx=Load()),
                                                        slice=Constant(value='identifier', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='protocol', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='is_probing',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=Name(id='connection', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='connection', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='protocol', ctx=Load()),
                                                            attr='measureCommand',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Attribute(
                                                            value=Name(id='protocol', ctx=Load()),
                                                            attr='commandTerminator',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='serial', ctx=Load()),
                                            attr='serialutil',
                                            ctx=Load(),
                                        ),
                                        attr='SerialTimeoutException',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Pass()],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Error while probing %s with protocol %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='device', ctx=Load()),
                                                                Attribute(
                                                                    value=Name(id='protocol', ctx=Load()),
                                                                    attr='name',
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
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
