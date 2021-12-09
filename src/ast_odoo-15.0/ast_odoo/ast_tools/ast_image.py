Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='binascii', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        ImportFrom(
            module='PIL',
            names=[
                alias(name='Image', asname=None),
                alias(name='ImageOps', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='PIL',
            names=[alias(name='IcoImagePlugin', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='random',
            names=[alias(name='randrange', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='Image', ctx=Load()),
                    attr='preinit',
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='Image', ctx=Load()),
                    attr='_initialized',
                    ctx=Store(),
                ),
            ],
            value=Constant(value=2, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='FILETYPE_BASE64_MAGICWORD', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value=b'/', kind=None),
                    Constant(value=b'R', kind=None),
                    Constant(value=b'i', kind=None),
                    Constant(value=b'P', kind=None),
                ],
                values=[
                    Constant(value='jpg', kind=None),
                    Constant(value='gif', kind=None),
                    Constant(value='png', kind=None),
                    Constant(value='svg+xml', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='EXIF_TAG_ORIENTATION', ctx=Store())],
            value=Constant(value=274, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='EXIF_TAG_ORIENTATION_TO_TRANSPOSE_METHODS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value=0, kind=None),
                    Constant(value=1, kind=None),
                    Constant(value=2, kind=None),
                    Constant(value=3, kind=None),
                    Constant(value=4, kind=None),
                    Constant(value=5, kind=None),
                    Constant(value=6, kind=None),
                    Constant(value=7, kind=None),
                    Constant(value=8, kind=None),
                ],
                values=[
                    List(elts=[], ctx=Load()),
                    List(elts=[], ctx=Load()),
                    List(
                        elts=[
                            Attribute(
                                value=Name(id='Image', ctx=Load()),
                                attr='FLIP_LEFT_RIGHT',
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Attribute(
                                value=Name(id='Image', ctx=Load()),
                                attr='ROTATE_180',
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Attribute(
                                value=Name(id='Image', ctx=Load()),
                                attr='FLIP_TOP_BOTTOM',
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Attribute(
                                value=Name(id='Image', ctx=Load()),
                                attr='FLIP_LEFT_RIGHT',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='Image', ctx=Load()),
                                attr='ROTATE_90',
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Attribute(
                                value=Name(id='Image', ctx=Load()),
                                attr='ROTATE_270',
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Attribute(
                                value=Name(id='Image', ctx=Load()),
                                attr='FLIP_TOP_BOTTOM',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='Image', ctx=Load()),
                                attr='ROTATE_90',
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    List(
                        elts=[
                            Attribute(
                                value=Name(id='Image', ctx=Load()),
                                attr='ROTATE_90',
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='IMAGE_MAX_RESOLUTION', ctx=Store())],
            value=Constant(value=45000000.0, kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='ImageProcess',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='base64_source', annotation=None, type_comment=None),
                            arg(arg='verify_resolution', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Initialize the `base64_source` image for processing.\n\n        :param base64_source: the original image base64 encoded\n            No processing will be done if the `base64_source` is falsy or if\n            the image is SVG.\n        :type base64_source: string or bytes\n\n        :param verify_resolution: if True, make sure the original image size is not\n            excessive before starting to process it. The max allowed resolution is\n            defined by `IMAGE_MAX_RESOLUTION`.\n        :type verify_resolution: bool\n\n        :return: self\n        :rtype: ImageProcess\n\n        :raise: ValueError if `verify_resolution` is True and the image is too large\n        :raise: UserError if the base64 is incorrect or the image can't be identified by PIL\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='base64_source',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='base64_source', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='operationsCount',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='base64_source', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='base64_source', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=1, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=b'P', kind=None),
                                                    Constant(value='P', kind=None),
                                                ],
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
                                            attr='image',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='image',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='base64_to_image', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='base64_source',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='original_format',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='image',
                                                            ctx=Load(),
                                                        ),
                                                        attr='format',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            attr='upper',
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
                                            attr='image',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='image_fix_orientation', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='image',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='w', ctx=Store()),
                                                Name(id='h', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='image',
                                            ctx=Load(),
                                        ),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='verify_resolution', ctx=Load()),
                                            Compare(
                                                left=BinOp(
                                                    left=Name(id='w', ctx=Load()),
                                                    op=Mult(),
                                                    right=Name(id='h', ctx=Load()),
                                                ),
                                                ops=[Gt()],
                                                comparators=[Name(id='IMAGE_MAX_RESOLUTION', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Image size excessive, uploaded images must be smaller than %s million pixels.', kind=None),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='IMAGE_MAX_RESOLUTION', ctx=Load()),
                                                                        op=Div(),
                                                                        right=Constant(value=10000000.0, kind=None),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='image_quality',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='quality', annotation=None, type_comment=None),
                            arg(arg='output_format', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value='', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return the image resulting of all the image processing\n        operations that have been applied previously.\n\n        Return False if the initialized `image` was falsy, and return\n        the initialized `image` without change if it was SVG.\n\n        Also return the initialized `image` if no operations have been applied\n        and the `output_format` is the same as the original format and the\n        quality is not specified.\n\n        :param quality: quality setting to apply. Default to 0.\n            - for JPEG: 1 is worse, 95 is best. Values above 95 should be\n                avoided. Falsy values will fallback to 95, but only if the image\n                was changed, otherwise the original image is returned.\n            - for PNG: set falsy to prevent conversion to a WEB palette.\n            - for other formats: no effect.\n        :type quality: int\n\n        :param output_format: the output format. Can be PNG, JPEG, GIF, or ICO.\n            Default to the format of the original image. BMP is converted to\n            PNG, other formats than those mentioned above are converted to JPEG.\n        :type output_format: string\n\n        :return: image\n        :rtype: bytes or False\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='image',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='image',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='output_image', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='image',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='output_format', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='output_format', ctx=Load()),
                                            attr='upper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='original_format',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='output_format', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='BMP', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='output_format', ctx=Store())],
                                    value=Constant(value='PNG', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='output_format', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='PNG', kind=None),
                                                    Constant(value='JPEG', kind=None),
                                                    Constant(value='GIF', kind=None),
                                                    Constant(value='ICO', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='output_format', ctx=Store())],
                                            value=Constant(value='JPEG', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='operationsCount',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Compare(
                                        left=Name(id='output_format', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='original_format',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='quality', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='image',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='opt', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='format', kind=None)],
                                values=[Name(id='output_format', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='output_format', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='PNG', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='opt', ctx=Load()),
                                            slice=Constant(value='optimize', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='quality', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='output_image', ctx=Load()),
                                                    attr='mode',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='P', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='output_image', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='output_image', ctx=Load()),
                                                                    attr='convert',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='RGBA', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='convert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='P', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='palette',
                                                                value=Attribute(
                                                                    value=Name(id='Image', ctx=Load()),
                                                                    attr='WEB',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='colors',
                                                                value=Constant(value=256, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='output_format', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='JPEG', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='opt', ctx=Load()),
                                            slice=Constant(value='optimize', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='opt', ctx=Load()),
                                            slice=Constant(value='quality', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='quality', ctx=Load()),
                                            Constant(value=95, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='output_format', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='GIF', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='opt', ctx=Load()),
                                            slice=Constant(value='optimize', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='opt', ctx=Load()),
                                            slice=Constant(value='save_all', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='output_image', ctx=Load()),
                                            attr='mode',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='1', kind=None),
                                                    Constant(value='L', kind=None),
                                                    Constant(value='P', kind=None),
                                                    Constant(value='RGB', kind=None),
                                                    Constant(value='RGBA', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='output_format', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='JPEG', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='output_image', ctx=Load()),
                                                    attr='mode',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='RGBA', kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='output_image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='output_image', ctx=Load()),
                                            attr='convert',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='RGB', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='image_apply_opt', ctx=Load()),
                                args=[Name(id='output_image', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='opt', ctx=Load()),
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
                    name='image_base64',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='quality', annotation=None, type_comment=None),
                            arg(arg='output_format', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value='', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return the base64 encoded image resulting of all the image processing\n        operations that have been applied previously.\n\n        Return False if the initialized `base64_source` was falsy, and return\n        the initialized `base64_source` without change if it was SVG.\n\n        Also return the initialized `base64_source` if no operations have been\n        applied and the `output_format` is the same as the original format and\n        the quality is not specified.\n\n        :param quality: quality setting to apply. Default to 0.\n            - for JPEG: 1 is worse, 95 is best. Values above 95 should be\n                avoided. Falsy values will fallback to 95, but only if the image\n                was changed, otherwise the original image is returned.\n            - for PNG: set falsy to prevent conversion to a WEB palette.\n            - for other formats: no effect.\n        :type quality: int\n\n        :param output_format: the output format. Can be PNG, JPEG, GIF, or ICO.\n            Default to the format of the original image. BMP is converted to\n            PNG, other formats than those mentioned above are converted to JPEG.\n        :type output_format: string\n\n        :return: image base64 encoded or False\n        :rtype: bytes or False\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='image',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='base64_source',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='stream', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='image_quality',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='quality',
                                        value=Name(id='quality', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='output_format',
                                        value=Name(id='output_format', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='stream', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='image',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stream', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='base64_source',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='resize',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='max_width', annotation=None, type_comment=None),
                            arg(arg='max_height', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Resize the image.\n\n        The image is never resized above the current image size. This method is\n        only to create a smaller version of the image.\n\n        The current ratio is preserved. To change the ratio, see `crop_resize`.\n\n        If `max_width` or `max_height` is falsy, it will be computed from the\n        other to keep the current ratio. If both are falsy, no resize is done.\n\n        It is currently not supported for GIF because we do not handle all the\n        frames properly.\n\n        :param max_width: max width\n        :type max_width: int\n\n        :param max_height: max height\n        :type max_height: int\n\n        :return: self to allow chaining\n        :rtype: ImageProcess\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='image',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='original_format',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='GIF', kind=None)],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='max_width', ctx=Load()),
                                            Name(id='max_height', ctx=Load()),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='w', ctx=Store()),
                                                Name(id='h', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='image',
                                            ctx=Load(),
                                        ),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='asked_width', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='max_width', ctx=Load()),
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='w', ctx=Load()),
                                                    op=Mult(),
                                                    right=Name(id='max_height', ctx=Load()),
                                                ),
                                                op=FloorDiv(),
                                                right=Name(id='h', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='asked_height', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='max_height', ctx=Load()),
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='h', ctx=Load()),
                                                    op=Mult(),
                                                    right=Name(id='max_width', ctx=Load()),
                                                ),
                                                op=FloorDiv(),
                                                right=Name(id='w', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Name(id='asked_width', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='w', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Name(id='asked_height', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='h', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='image',
                                                        ctx=Load(),
                                                    ),
                                                    attr='thumbnail',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='asked_width', ctx=Load()),
                                                            Name(id='asked_height', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='Image', ctx=Load()),
                                                        attr='LANCZOS',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='image',
                                                                ctx=Load(),
                                                            ),
                                                            attr='width',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='w', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='image',
                                                                ctx=Load(),
                                                            ),
                                                            attr='height',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='h', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='operationsCount',
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='self', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='crop_resize',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='max_width', annotation=None, type_comment=None),
                            arg(arg='max_height', annotation=None, type_comment=None),
                            arg(arg='center_x', annotation=None, type_comment=None),
                            arg(arg='center_y', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0.5, kind=None),
                            Constant(value=0.5, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Crop and resize the image.\n\n        The image is never resized above the current image size. This method is\n        only to create smaller versions of the image.\n\n        Instead of preserving the ratio of the original image like `resize`,\n        this method will force the output to take the ratio of the given\n        `max_width` and `max_height`, so both have to be defined.\n\n        The crop is done before the resize in order to preserve as much of the\n        original image as possible. The goal of this method is primarily to\n        resize to a given ratio, and it is not to crop unwanted parts of the\n        original image. If the latter is what you want to do, you should create\n        another method, or directly use the `crop` method from PIL.\n\n        It is currently not supported for GIF because we do not handle all the\n        frames properly.\n\n        :param max_width: max width\n        :type max_width: int\n\n        :param max_height: max height\n        :type max_height: int\n\n        :param center_x: the center of the crop between 0 (left) and 1 (right)\n            Default to 0.5 (center).\n        :type center_x: float\n\n        :param center_y: the center of the crop between 0 (top) and 1 (bottom)\n            Default to 0.5 (center).\n        :type center_y: float\n\n        :return: self to allow chaining\n        :rtype: ImageProcess\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='image',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='original_format',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='GIF', kind=None)],
                                    ),
                                    Name(id='max_width', ctx=Load()),
                                    Name(id='max_height', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='w', ctx=Store()),
                                                Name(id='h', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='image',
                                            ctx=Load(),
                                        ),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='w', ctx=Load()),
                                            op=Div(),
                                            right=Name(id='max_width', ctx=Load()),
                                        ),
                                        ops=[Gt()],
                                        comparators=[
                                            BinOp(
                                                left=Name(id='h', ctx=Load()),
                                                op=Div(),
                                                right=Name(id='max_height', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='new_w', ctx=Store()),
                                                        Name(id='new_h', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='w', ctx=Load()),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='max_height', ctx=Load()),
                                                            op=Mult(),
                                                            right=Name(id='w', ctx=Load()),
                                                        ),
                                                        op=FloorDiv(),
                                                        right=Name(id='max_width', ctx=Load()),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='new_w', ctx=Store()),
                                                        Name(id='new_h', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='max_width', ctx=Load()),
                                                            op=Mult(),
                                                            right=Name(id='h', ctx=Load()),
                                                        ),
                                                        op=FloorDiv(),
                                                        right=Name(id='max_height', ctx=Load()),
                                                    ),
                                                    Name(id='h', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='new_w', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Name(id='w', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='new_w', ctx=Store()),
                                                        Name(id='new_h', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='w', ctx=Load()),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='new_h', ctx=Load()),
                                                            op=Mult(),
                                                            right=Name(id='w', ctx=Load()),
                                                        ),
                                                        op=FloorDiv(),
                                                        right=Name(id='new_w', ctx=Load()),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='new_h', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Name(id='h', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='new_w', ctx=Store()),
                                                        Name(id='new_h', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='new_w', ctx=Load()),
                                                            op=Mult(),
                                                            right=Name(id='h', ctx=Load()),
                                                        ),
                                                        op=FloorDiv(),
                                                        right=Name(id='new_h', ctx=Load()),
                                                    ),
                                                    Name(id='h', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='x_offset', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='w', ctx=Load()),
                                                    op=Sub(),
                                                    right=Name(id='new_w', ctx=Load()),
                                                ),
                                                op=Mult(),
                                                right=Name(id='center_x', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='h_offset', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='h', ctx=Load()),
                                                    op=Sub(),
                                                    right=Name(id='new_h', ctx=Load()),
                                                ),
                                                op=Mult(),
                                                right=Name(id='center_y', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Name(id='new_w', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='w', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Name(id='new_h', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='h', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='image',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='image',
                                                        ctx=Load(),
                                                    ),
                                                    attr='crop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='x_offset', ctx=Load()),
                                                            Name(id='h_offset', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='x_offset', ctx=Load()),
                                                                op=Add(),
                                                                right=Name(id='new_w', ctx=Load()),
                                                            ),
                                                            BinOp(
                                                                left=Name(id='h_offset', ctx=Load()),
                                                                op=Add(),
                                                                right=Name(id='new_h', ctx=Load()),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='image',
                                                                ctx=Load(),
                                                            ),
                                                            attr='width',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='w', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='image',
                                                                ctx=Load(),
                                                            ),
                                                            attr='height',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='h', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='operationsCount',
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='resize',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='max_width', ctx=Load()),
                                    Name(id='max_height', ctx=Load()),
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
                    name='colorize',
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
                            value=Constant(value='Replace the transparent background by a random color.\n\n        :return: self to allow chaining\n        :rtype: ImageProcess\n        ', kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='image',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='original', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='image',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='color', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='randrange', ctx=Load()),
                                                args=[
                                                    Constant(value=32, kind=None),
                                                    Constant(value=224, kind=None),
                                                    Constant(value=24, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='randrange', ctx=Load()),
                                                args=[
                                                    Constant(value=32, kind=None),
                                                    Constant(value=224, kind=None),
                                                    Constant(value=24, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='randrange', ctx=Load()),
                                                args=[
                                                    Constant(value=32, kind=None),
                                                    Constant(value=224, kind=None),
                                                    Constant(value=24, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='image',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='RGB', kind=None),
                                            Attribute(
                                                value=Name(id='original', ctx=Load()),
                                                attr='size',
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
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='image',
                                                ctx=Load(),
                                            ),
                                            attr='paste',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='color', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='box',
                                                value=BinOp(
                                                    left=Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Attribute(
                                                        value=Name(id='original', ctx=Load()),
                                                        attr='size',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='image',
                                                ctx=Load(),
                                            ),
                                            attr='paste',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='original', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='mask',
                                                value=Name(id='original', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='operationsCount',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='self', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='image_process',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='base64_source', annotation=None, type_comment=None),
                    arg(arg='size', annotation=None, type_comment=None),
                    arg(arg='verify_resolution', annotation=None, type_comment=None),
                    arg(arg='quality', annotation=None, type_comment=None),
                    arg(arg='crop', annotation=None, type_comment=None),
                    arg(arg='colorize', annotation=None, type_comment=None),
                    arg(arg='output_format', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Tuple(
                        elts=[
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Constant(value=False, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                    Constant(value='', kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Process the `base64_source` image by executing the given operations and\n    return the result as a base64 encoded image.\n    ', kind=None),
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='base64_source', ctx=Load()),
                            ),
                            BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='size', ctx=Load()),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Subscript(
                                                            value=Name(id='size', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Subscript(
                                                            value=Name(id='size', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='verify_resolution', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='quality', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='crop', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='colorize', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='output_format', ctx=Load()),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Name(id='base64_source', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='image', ctx=Store())],
                    value=Call(
                        func=Name(id='ImageProcess', ctx=Load()),
                        args=[
                            Name(id='base64_source', ctx=Load()),
                            Name(id='verify_resolution', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='size', ctx=Load()),
                    body=[
                        If(
                            test=Name(id='crop', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='center_x', ctx=Store())],
                                    value=Constant(value=0.5, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='center_y', ctx=Store())],
                                    value=Constant(value=0.5, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='crop', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='top', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='center_y', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='crop', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='bottom', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='center_y', ctx=Store())],
                                                    value=Constant(value=1, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='image', ctx=Load()),
                                            attr='crop_resize',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='max_width',
                                                value=Subscript(
                                                    value=Name(id='size', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='max_height',
                                                value=Subscript(
                                                    value=Name(id='size', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='center_x',
                                                value=Name(id='center_x', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='center_y',
                                                value=Name(id='center_y', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='image', ctx=Load()),
                                            attr='resize',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='max_width',
                                                value=Subscript(
                                                    value=Name(id='size', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='max_height',
                                                value=Subscript(
                                                    value=Name(id='size', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Name(id='colorize', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='image', ctx=Load()),
                                    attr='colorize',
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
                    value=Call(
                        func=Attribute(
                            value=Name(id='image', ctx=Load()),
                            attr='image_base64',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='quality',
                                value=Name(id='quality', ctx=Load()),
                            ),
                            keyword(
                                arg='output_format',
                                value=Name(id='output_format', ctx=Load()),
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
            name='average_dominant_color',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='colors', annotation=None, type_comment=None),
                    arg(arg='mitigate', annotation=None, type_comment=None),
                    arg(arg='max_margin', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=175, kind=None),
                    Constant(value=140, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='This function is used to calculate the dominant colors when given a list of colors\n\n    There are 5 steps :\n        1) Select dominant colors (highest count), isolate its values and remove\n           it from the current color set.\n        2) Set margins according to the prevalence of the dominant color.\n        3) Evaluate the colors. Similar colors are grouped in the dominant set\n           while others are put in the "remaining" list.\n        4) Calculate the average color for the dominant set. This is done by\n           averaging each band and joining them into a tuple.\n        5) Mitigate final average and convert it to hex\n\n    :param colors: list of tuples having:\n        [0] color count in the image\n        [1] actual color: tuple(R, G, B, A)\n        -> these can be extracted from a PIL image using image.getcolors()\n    :param mitigate: maximum value a band can reach\n    :param max_margin: maximum difference from one of the dominant values\n    :returns: a tuple with two items:\n        [0] the average color of the dominant set as: tuple(R, G, B)\n        [1] list of remaining colors, used to evaluate subsequent dominant colors\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='dominant_color', ctx=Store())],
                    value=Call(
                        func=Name(id='max', ctx=Load()),
                        args=[Name(id='colors', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dominant_rgb', ctx=Store())],
                    value=Subscript(
                        value=Subscript(
                            value=Name(id='dominant_color', ctx=Load()),
                            slice=Constant(value=1, kind=None),
                            ctx=Load(),
                        ),
                        slice=Slice(
                            lower=None,
                            upper=Constant(value=3, kind=None),
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dominant_set', ctx=Store())],
                    value=List(
                        elts=[Name(id='dominant_color', ctx=Load())],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='remaining', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='margins', ctx=Store())],
                    value=BinOp(
                        left=List(
                            elts=[
                                BinOp(
                                    left=Name(id='max_margin', ctx=Load()),
                                    op=Mult(),
                                    right=BinOp(
                                        left=Constant(value=1, kind=None),
                                        op=Sub(),
                                        right=BinOp(
                                            left=Subscript(
                                                value=Name(id='dominant_color', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            op=Div(),
                                            right=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    ListComp(
                                                        elt=Subscript(
                                                            value=Name(id='col', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='col', ctx=Store()),
                                                                iter=Name(id='colors', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                ),
                            ],
                            ctx=Load(),
                        ),
                        op=Mult(),
                        right=Constant(value=3, kind=None),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='colors', ctx=Load()),
                            attr='remove',
                            ctx=Load(),
                        ),
                        args=[Name(id='dominant_color', ctx=Load())],
                        keywords=[],
                    ),
                ),
                For(
                    target=Name(id='color', ctx=Store()),
                    iter=Name(id='colors', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='rgb', ctx=Store())],
                            value=Subscript(
                                value=Name(id='color', ctx=Load()),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='rgb', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='dominant_rgb', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='margins', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='rgb', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='dominant_rgb', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Subscript(
                                                    value=Name(id='margins', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='rgb', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='dominant_rgb', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='margins', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='rgb', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='dominant_rgb', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Subscript(
                                                    value=Name(id='margins', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='rgb', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='dominant_rgb', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='margins', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='rgb', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='dominant_rgb', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Subscript(
                                                    value=Name(id='margins', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dominant_set', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='color', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='remaining', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='color', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dominant_avg', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='band', ctx=Store()),
                    iter=Call(
                        func=Name(id='range', ctx=Load()),
                        args=[Constant(value=3, kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Name(id='avg', ctx=Store()),
                                Name(id='total', ctx=Store()),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='color', ctx=Store()),
                            iter=Name(id='dominant_set', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='avg', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='color', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Subscript(
                                            value=Subscript(
                                                value=Name(id='color', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='band', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='total', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Name(id='color', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dominant_avg', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='avg', ctx=Load()),
                                                op=Div(),
                                                right=Name(id='total', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='final_dominant', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='brightest', ctx=Store())],
                    value=Call(
                        func=Name(id='max', ctx=Load()),
                        args=[Name(id='dominant_avg', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='color', ctx=Store()),
                    iter=Call(
                        func=Name(id='range', ctx=Load()),
                        args=[Constant(value=3, kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='brightest', ctx=Load()),
                                    ops=[Gt()],
                                    comparators=[Name(id='mitigate', ctx=Load())],
                                ),
                                body=BinOp(
                                    left=Subscript(
                                        value=Name(id='dominant_avg', ctx=Load()),
                                        slice=Name(id='color', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    op=Div(),
                                    right=BinOp(
                                        left=Name(id='brightest', ctx=Load()),
                                        op=Div(),
                                        right=Name(id='mitigate', ctx=Load()),
                                    ),
                                ),
                                orelse=Subscript(
                                    value=Name(id='dominant_avg', ctx=Load()),
                                    slice=Name(id='color', ctx=Load()),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='final_dominant', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
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
                    value=Tuple(
                        elts=[
                            Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[Name(id='final_dominant', ctx=Load())],
                                keywords=[],
                            ),
                            Name(id='remaining', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='image_fix_orientation',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='image', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Fix the orientation of the image if it has an EXIF orientation tag.\n\n    This typically happens for images taken from a non-standard orientation\n    by some phones or other devices that are able to report orientation.\n\n    The specified transposition is applied to the image before all other\n    operations, because all of them expect the image to be in its final\n    orientation, which is the case only when the first row of pixels is the top\n    of the image and the first column of pixels is the left of the image.\n\n    Moreover the EXIF tags will not be kept when the image is later saved, so\n    the transposition has to be done to ensure the final image is correctly\n    orientated.\n\n    Note: to be completely correct, the resulting image should have its exif\n    orientation tag removed, since the transpositions have been applied.\n    However since this tag is not used in the code, it is acceptable to\n    save the complexity of removing it.\n\n    :param image: the source image\n    :type image: PIL.Image\n\n    :return: the resulting image, copy of the source, with orientation fixed\n        or the source image if no operation was applied\n    :rtype: PIL.Image\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='getexif', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='image', ctx=Load()),
                                    Constant(value='getexif', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='image', ctx=Load()),
                                    Constant(value='_getexif', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='getexif', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='exif', ctx=Store())],
                            value=Call(
                                func=Name(id='getexif', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='exif', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='orientation', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='exif', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='EXIF_TAG_ORIENTATION', ctx=Load()),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='method', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='EXIF_TAG_ORIENTATION_TO_TRANSPOSE_METHODS', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='orientation', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='image', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='image', ctx=Load()),
                                                    attr='transpose',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='method', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='image', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='image', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='base64_to_image',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='base64_source', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value="Return a PIL image from the given `base64_source`.\n\n    :param base64_source: the image base64 encoded\n    :type base64_source: string or bytes\n\n    :return: the PIL image\n    :rtype: PIL.Image\n\n    :raise: UserError if the base64 is incorrect or the image can't be identified by PIL\n    ", kind=None),
                ),
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='base64_source', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Tuple(
                                elts=[
                                    Name(id='OSError', ctx=Load()),
                                    Attribute(
                                        value=Name(id='binascii', ctx=Load()),
                                        attr='Error',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            name=None,
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This file could not be decoded as an image file. Please try with a different file.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
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
            name='image_apply_opt',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='image', annotation=None, type_comment=None),
                    arg(arg='format', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='params', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Return the given PIL `image` using `params`.\n\n    :param image: the PIL image\n    :type image: PIL.Image\n\n    :param params: params to expand when calling PIL.Image.save()\n    :type params: dict\n\n    :return: the image formatted\n    :rtype: bytes\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='stream', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='io', ctx=Load()),
                            attr='BytesIO',
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
                            value=Name(id='image', ctx=Load()),
                            attr='save',
                            ctx=Load(),
                        ),
                        args=[Name(id='stream', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='format',
                                value=Name(id='format', ctx=Load()),
                            ),
                            keyword(
                                arg=None,
                                value=Name(id='params', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='stream', ctx=Load()),
                            attr='getvalue',
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
            name='image_to_base64',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='image', annotation=None, type_comment=None),
                    arg(arg='format', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='params', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Return a base64_image from the given PIL `image` using `params`.\n\n    :param image: the PIL image\n    :type image: PIL.Image\n\n    :param params: params to expand when calling PIL.Image.save()\n    :type params: dict\n\n    :return: the image base64 encoded\n    :rtype: bytes\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='stream', ctx=Store())],
                    value=Call(
                        func=Name(id='image_apply_opt', ctx=Load()),
                        args=[
                            Name(id='image', ctx=Load()),
                            Name(id='format', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg=None,
                                value=Name(id='params', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='base64', ctx=Load()),
                            attr='b64encode',
                            ctx=Load(),
                        ),
                        args=[Name(id='stream', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='is_image_size_above',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='base64_source_1', annotation=None, type_comment=None),
                    arg(arg='base64_source_2', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Return whether or not the size of the given image `base64_source_1` is\n    above the size of the given image `base64_source_2`.\n    ', kind=None),
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='base64_source_1', ctx=Load()),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='base64_source_2', ctx=Load()),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Subscript(
                                    value=Name(id='base64_source_1', ctx=Load()),
                                    slice=Slice(
                                        lower=None,
                                        upper=Constant(value=1, kind=None),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=b'P', kind=None),
                                            Constant(value='P', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            Compare(
                                left=Subscript(
                                    value=Name(id='base64_source_2', ctx=Load()),
                                    slice=Slice(
                                        lower=None,
                                        upper=Constant(value=1, kind=None),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=b'P', kind=None),
                                            Constant(value='P', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='image_source', ctx=Store())],
                    value=Call(
                        func=Name(id='image_fix_orientation', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='base64_to_image', ctx=Load()),
                                args=[Name(id='base64_source_1', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_target', ctx=Store())],
                    value=Call(
                        func=Name(id='image_fix_orientation', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='base64_to_image', ctx=Load()),
                                args=[Name(id='base64_source_2', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Attribute(
                                    value=Name(id='image_source', ctx=Load()),
                                    attr='width',
                                    ctx=Load(),
                                ),
                                ops=[Gt()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='image_target', ctx=Load()),
                                        attr='width',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            Compare(
                                left=Attribute(
                                    value=Name(id='image_source', ctx=Load()),
                                    attr='height',
                                    ctx=Load(),
                                ),
                                ops=[Gt()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='image_target', ctx=Load()),
                                        attr='height',
                                        ctx=Load(),
                                    ),
                                ],
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
            name='image_guess_size_from_field_name',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='field_name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value="Attempt to guess the image size based on `field_name`.\n\n    If it can't be guessed, return (0, 0) instead.\n\n    :param field_name: the name of a field\n    :type field_name: string\n\n    :return: the guessed size\n    :rtype: tuple (width, height)\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='suffix', ctx=Store())],
                    value=IfExp(
                        test=Compare(
                            left=Name(id='field_name', ctx=Load()),
                            ops=[Eq()],
                            comparators=[Constant(value='image', kind=None)],
                        ),
                        body=Constant(value='1024', kind=None),
                        orelse=Subscript(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='field_name', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='_', kind=None)],
                                keywords=[],
                            ),
                            slice=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='suffix', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='suffix', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='ValueError', ctx=Load()),
                            name=None,
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
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
            name='image_data_uri',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='base64_source', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='This returns data URL scheme according RFC 2397\n    (https://tools.ietf.org/html/rfc2397) for all kind of supported images\n    (PNG, GIF, JPG and SVG), defaulting on PNG type if not mimetype detected.\n    ', kind=None),
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='data:image/%s;base64,%s', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='FILETYPE_BASE64_MAGICWORD', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Subscript(
                                            value=Name(id='base64_source', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=1, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Constant(value='png', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                Call(
                                    func=Attribute(
                                        value=Name(id='base64_source', ctx=Load()),
                                        attr='decode',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_saturation',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='rgb', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Returns the saturation (hsl format) of a given rgb color\n\n    :param rgb: rgb tuple or list\n    :return: saturation\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='c_max', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Name(id='max', ctx=Load()),
                            args=[Name(id='rgb', ctx=Load())],
                            keywords=[],
                        ),
                        op=Div(),
                        right=Constant(value=255, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='c_min', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Name(id='min', ctx=Load()),
                            args=[Name(id='rgb', ctx=Load())],
                            keywords=[],
                        ),
                        op=Div(),
                        right=Constant(value=255, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='d', ctx=Store())],
                    value=BinOp(
                        left=Name(id='c_max', ctx=Load()),
                        op=Sub(),
                        right=Name(id='c_min', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=IfExp(
                        test=Compare(
                            left=Name(id='d', ctx=Load()),
                            ops=[Eq()],
                            comparators=[Constant(value=0, kind=None)],
                        ),
                        body=Constant(value=0, kind=None),
                        orelse=BinOp(
                            left=Name(id='d', ctx=Load()),
                            op=Div(),
                            right=BinOp(
                                left=Constant(value=1, kind=None),
                                op=Sub(),
                                right=Call(
                                    func=Name(id='abs', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=BinOp(
                                                left=Name(id='c_max', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='c_min', ctx=Load()),
                                            ),
                                            op=Sub(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_lightness',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='rgb', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Returns the lightness (hsl format) of a given rgb color\n\n    :param rgb: rgb tuple or list\n    :return: lightness\n    ', kind=None),
                ),
                Return(
                    value=BinOp(
                        left=BinOp(
                            left=BinOp(
                                left=Call(
                                    func=Name(id='max', ctx=Load()),
                                    args=[Name(id='rgb', ctx=Load())],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='min', ctx=Load()),
                                    args=[Name(id='rgb', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            op=Div(),
                            right=Constant(value=2, kind=None),
                        ),
                        op=Div(),
                        right=Constant(value=255, kind=None),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='hex_to_rgb',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='hx', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value="Converts an hexadecimal string (starting with '#') to a RGB tuple", kind=None),
                ),
                Return(
                    value=Call(
                        func=Name(id='tuple', ctx=Load()),
                        args=[
                            ListComp(
                                elt=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='hx', ctx=Load()),
                                            slice=Slice(
                                                lower=Name(id='i', ctx=Load()),
                                                upper=BinOp(
                                                    left=Name(id='i', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value=2, kind=None),
                                                ),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        Constant(value=16, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='i', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[
                                                Constant(value=1, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=2, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
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
            name='rgb_to_hex',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='rgb', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Converts a RGB tuple or list to an hexadecimal string', kind=None),
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='#', kind=None),
                        op=Add(),
                        right=Call(
                            func=Attribute(
                                value=Constant(value='', kind=None),
                                attr='join',
                                ctx=Load(),
                            ),
                            args=[
                                ListComp(
                                    elt=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Name(id='hex', ctx=Load()),
                                                            args=[Name(id='c', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='x', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='zfill',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2, kind=None)],
                                        keywords=[],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='c', ctx=Store()),
                                            iter=Name(id='rgb', ctx=Load()),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                Import(
                    names=[alias(name='sys', asname=None)],
                ),
                Assert(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[
                                Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='argv',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value=3, kind=None)],
                    ),
                    msg=Constant(value='Usage to Test: image.py SRC.png DEST.png', kind=None),
                ),
                Assign(
                    targets=[Name(id='img', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='base64', ctx=Load()),
                            attr='b64encode',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='sys', ctx=Load()),
                                                    attr='argv',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
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
                    targets=[Name(id='new', ctx=Store())],
                    value=Call(
                        func=Name(id='image_process', ctx=Load()),
                        args=[Name(id='img', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='size',
                                value=Tuple(
                                    elts=[
                                        Constant(value=128, kind=None),
                                        Constant(value=100, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='open', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='sys', ctx=Load()),
                                            attr='argv',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='wb', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='write',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='new', ctx=Load())],
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
    type_ignores=[],
)
