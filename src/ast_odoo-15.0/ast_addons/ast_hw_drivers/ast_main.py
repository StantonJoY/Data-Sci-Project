Module(
    body=[
        ImportFrom(
            module='traceback',
            names=[alias(name='format_exc', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dbus.mainloop.glib',
            names=[alias(name='DBusGMainLoop', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='socket', asname=None)],
        ),
        ImportFrom(
            module='threading',
            names=[alias(name='Thread', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='urllib3', asname=None)],
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
            targets=[Name(id='drivers', ctx=Store())],
            value=List(elts=[], ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='interfaces', ctx=Store())],
            value=Dict(keys=[], values=[]),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='iot_devices', ctx=Store())],
            value=Dict(keys=[], values=[]),
            type_comment=None,
        ),
        ClassDef(
            name='Manager',
            bases=[Name(id='Thread', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='send_alldevices',
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
                            value=Constant(value='\n        This method send IoT Box and devices informations to Odoo database\n        ', kind=None),
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
                        If(
                            test=Name(id='server', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='subject', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='helpers', ctx=Load()),
                                            attr='read_file_first_line',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='odoo-subject.conf', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='subject', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='helpers', ctx=Load()),
                                                                attr='get_ip',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='replace',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='.', kind=None),
                                                        Constant(value='-', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='subject', ctx=Load()),
                                                        attr='strip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='*', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='get_ip',
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
                                    targets=[Name(id='iot_box', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='identifier', kind=None),
                                            Constant(value='ip', kind=None),
                                            Constant(value='token', kind=None),
                                            Constant(value='version', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='socket', ctx=Load()),
                                                    attr='gethostname',
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
                                            Name(id='domain', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='helpers', ctx=Load()),
                                                    attr='get_token',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
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
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='devices_list', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='device', ctx=Store()),
                                    iter=Name(id='iot_devices', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='identifier', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='iot_devices', ctx=Load()),
                                                    slice=Name(id='device', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='device_identifier',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='devices_list', ctx=Load()),
                                                    slice=Name(id='identifier', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='manufacturer', kind=None),
                                                    Constant(value='connection', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='iot_devices', ctx=Load()),
                                                            slice=Name(id='device', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='device_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='iot_devices', ctx=Load()),
                                                            slice=Name(id='device', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='device_type',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='iot_devices', ctx=Load()),
                                                            slice=Name(id='device', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='device_manufacturer',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='iot_devices', ctx=Load()),
                                                            slice=Name(id='device', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='device_connection',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='data', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='params', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='iot_box', kind=None),
                                                    Constant(value='devices', kind=None),
                                                ],
                                                values=[
                                                    Name(id='iot_box', ctx=Load()),
                                                    Name(id='devices_list', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='http', ctx=Load()),
                                                    attr='request',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='POST', kind=None),
                                                    BinOp(
                                                        left=Name(id='server', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value='/iot/setup', kind=None),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='json', ctx=Load()),
                                                                        attr='dumps',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='data', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                attr='encode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='utf8', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='headers',
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='Content-type', kind=None),
                                                                Constant(value='Accept', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='application/json', kind=None),
                                                                Constant(value='text/plain', kind=None),
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
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Odoo server not set', kind=None)],
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
                            value=Constant(value='\n        Thread that will load interfaces and drivers and contact the odoo server with the updates\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='check_git_branch',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='send_alldevices',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='download_iot_handlers',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='helpers', ctx=Load()),
                                    attr='load_iot_handlers',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='interface', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='interfaces', ctx=Load()),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='i', ctx=Store())],
                                    value=Call(
                                        func=Name(id='interface', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='i', ctx=Load()),
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
                                            value=Name(id='i', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='previous_iot_devices',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=Constant(value=1, kind=None),
                            body=[
                                Try(
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='iot_devices', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='previous_iot_devices',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='send_alldevices',
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
                                                            attr='previous_iot_devices',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='iot_devices', ctx=Load()),
                                                            attr='copy',
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
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=None,
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='format_exc', ctx=Load()),
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
                                    orelse=[],
                                    finalbody=[],
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
        Expr(
            value=Call(
                func=Name(id='DBusGMainLoop', ctx=Load()),
                args=[],
                keywords=[
                    keyword(
                        arg='set_as_default',
                        value=Constant(value=True, kind=None),
                    ),
                ],
            ),
        ),
        Assign(
            targets=[Name(id='manager', ctx=Store())],
            value=Call(
                func=Name(id='Manager', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='manager', ctx=Load()),
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
                    value=Name(id='manager', ctx=Load()),
                    attr='start',
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
        ),
    ],
    type_ignores=[],
)
