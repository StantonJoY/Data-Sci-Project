Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='pathlib',
            names=[alias(name='Path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='reportlab.graphics.shapes',
            names=[alias(name='Image', asname='ReportLabImage')],
            level=0,
        ),
        ImportFrom(
            module='reportlab.lib.units',
            names=[alias(name='mm', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='CH_QR_CROSS_SIZE_RATIO', ctx=Store())],
            value=Constant(value=0.1214, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='CH_QR_CROSS_FILE', ctx=Store())],
            value=Call(
                func=Name(id='Path', ctx=Load()),
                args=[Constant(value='../static/src/img/CH-Cross_7mm.png', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='IrActionsReport',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.actions.report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_available_barcode_masks',
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
                            targets=[Name(id='rslt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrActionsReport', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_available_barcode_masks',
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
                                    value=Name(id='rslt', ctx=Load()),
                                    slice=Constant(value='ch_cross', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='apply_qr_code_ch_cross_mask',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='rslt', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='apply_qr_code_ch_cross_mask',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='width', annotation=None, type_comment=None),
                            arg(arg='height', annotation=None, type_comment=None),
                            arg(arg='barcode_drawing', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cross_width', ctx=Store())],
                            value=BinOp(
                                left=Name(id='CH_QR_CROSS_SIZE_RATIO', ctx=Load()),
                                op=Mult(),
                                right=Name(id='width', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cross_height', ctx=Store())],
                            value=BinOp(
                                left=Name(id='CH_QR_CROSS_SIZE_RATIO', ctx=Load()),
                                op=Mult(),
                                right=Name(id='height', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cross_path', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='Path', ctx=Load()),
                                                args=[Name(id='__file__', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='absolute',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='parent',
                                    ctx=Load(),
                                ),
                                op=Div(),
                                right=Name(id='CH_QR_CROSS_FILE', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='qr_cross', ctx=Store())],
                            value=Call(
                                func=Name(id='ReportLabImage', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Name(id='width', ctx=Load()),
                                                op=Div(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                            op=Sub(),
                                            right=BinOp(
                                                left=Name(id='cross_width', ctx=Load()),
                                                op=Div(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                        ),
                                        op=Div(),
                                        right=Name(id='mm', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Name(id='height', ctx=Load()),
                                                op=Div(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                            op=Sub(),
                                            right=BinOp(
                                                left=Name(id='cross_height', ctx=Load()),
                                                op=Div(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                        ),
                                        op=Div(),
                                        right=Name(id='mm', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='cross_width', ctx=Load()),
                                        op=Div(),
                                        right=Name(id='mm', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='cross_height', ctx=Load()),
                                        op=Div(),
                                        right=Name(id='mm', ctx=Load()),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='cross_path', ctx=Load()),
                                            attr='as_posix',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='barcode_drawing', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[Name(id='qr_cross', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
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
