Module(
    body=[
        ImportFrom(
            module='glob',
            names=[alias(name='glob', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.interface',
            names=[alias(name='Interface', asname=None)],
            level=0,
        ),
        ClassDef(
            name='SerialInterface',
            bases=[Name(id='Interface', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='connection_type', ctx=Store())],
                    value=Constant(value='serial', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_devices',
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
                            targets=[Name(id='serial_devices', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='identifier', ctx=Store()),
                            iter=Call(
                                func=Name(id='glob', ctx=Load()),
                                args=[Constant(value='/dev/serial/by-path/*', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='serial_devices', ctx=Load()),
                                            slice=Name(id='identifier', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[Constant(value='identifier', kind=None)],
                                        values=[Name(id='identifier', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='serial_devices', ctx=Load()),
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
