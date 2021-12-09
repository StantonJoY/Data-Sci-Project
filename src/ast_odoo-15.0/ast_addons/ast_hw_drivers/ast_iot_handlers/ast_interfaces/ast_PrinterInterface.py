Module(
    body=[
        ImportFrom(
            module='cups',
            names=[alias(name='Connection', asname='cups_connection')],
            level=0,
        ),
        ImportFrom(
            module='re',
            names=[alias(name='sub', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='threading',
            names=[alias(name='Lock', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hw_drivers.interface',
            names=[alias(name='Interface', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='conn', ctx=Store())],
            value=Call(
                func=Name(id='cups_connection', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='PPDs', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='conn', ctx=Load()),
                    attr='getPPDs',
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='cups_lock', ctx=Store())],
            value=Call(
                func=Name(id='Lock', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='PrinterInterface',
            bases=[Name(id='Interface', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_loop_delay', ctx=Store())],
                    value=Constant(value=120, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='connection_type', ctx=Store())],
                    value=Constant(value='printer', kind=None),
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
                            targets=[Name(id='printer_devices', ctx=Store())],
                            value=Dict(keys=[], values=[]),
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
                                Assign(
                                    targets=[Name(id='printers', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='getPrinters',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='devices', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='conn', ctx=Load()),
                                            attr='getDevices',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='printer', ctx=Store()),
                                    iter=Name(id='printers', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='printers', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='printer', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='device-uri', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='path', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='path', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='devices', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='devices', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='path', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='supported', kind=None)],
                                                                values=[Constant(value=True, kind=None)],
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
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='path', ctx=Store()),
                            iter=Name(id='devices', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='uuid=', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='path', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='identifier', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sub', ctx=Load()),
                                                args=[
                                                    Constant(value='[^a-zA-Z0-9_]', kind=None),
                                                    Constant(value='', kind=None),
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='path', ctx=Load()),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='uuid=', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='serial=', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='path', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='identifier', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='sub', ctx=Load()),
                                                        args=[
                                                            Constant(value='[^a-zA-Z0-9_]', kind=None),
                                                            Constant(value='', kind=None),
                                                            Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='path', ctx=Load()),
                                                                        attr='split',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='serial=', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='identifier', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='sub', ctx=Load()),
                                                        args=[
                                                            Constant(value='[^a-zA-Z0-9_]', kind=None),
                                                            Constant(value='', kind=None),
                                                            Name(id='path', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='devices', ctx=Load()),
                                                slice=Name(id='path', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='identifier', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='identifier', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='devices', ctx=Load()),
                                                slice=Name(id='path', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='url', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='path', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='printer_devices', ctx=Load()),
                                            slice=Name(id='identifier', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='devices', ctx=Load()),
                                        slice=Name(id='path', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='printer_devices', ctx=Load()),
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
