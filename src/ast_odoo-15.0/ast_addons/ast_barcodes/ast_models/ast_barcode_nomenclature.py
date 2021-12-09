Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='UPC_EAN_CONVERSIONS', ctx=Store())],
            value=List(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='none', kind=None),
                            Constant(value='Never', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ean2upc', kind=None),
                            Constant(value='EAN-13 to UPC-A', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='upc2ean', kind=None),
                            Constant(value='UPC-A to EAN-13', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='always', kind=None),
                            Constant(value='Always', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='BarcodeNomenclature',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='barcode.nomenclature', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Barcode Nomenclature', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Barcode Nomenclature', kind=None),
                            ),
                            keyword(
                                arg='size',
                                value=Constant(value=32, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='An internal identification of the barcode nomenclature', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rule_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='barcode.rule', kind=None),
                            Constant(value='barcode_nomenclature_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Rules', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The list of barcode rules', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='upc_ean_conv', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='UPC_EAN_CONVERSIONS', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='UPC/EAN Conversion', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='always', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='UPC Codes can be converted to EAN by prefixing them with a zero. This setting determines if a UPC/EAN barcode should be automatically converted in one way or another when trying to match a rule with the other encoding.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_barcode_check_digit',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='numeric_barcode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Computes and returns the barcode check digit. The used algorithm\n        follows the GTIN specifications and can be used by all compatible\n        barcode nomenclature, like as EAN-8, EAN-12 (UPC-A) or EAN-13.\n\n        https://www.gs1.org/sites/default/files/docs/barcodes/GS1_General_Specifications.pdf\n        https://www.gs1.org/services/how-calculate-check-digit-manually\n\n        :param numeric_barcode: the barcode to verify/recompute the check digit\n        :type numeric_barcode: str\n        :return: the number corresponding to the right check digit\n        :rtype: int\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Name(id='oddsum', ctx=Store()),
                                Name(id='evensum', ctx=Store()),
                                Name(id='total', ctx=Store()),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Subscript(
                                value=Name(id='numeric_barcode', ctx=Load()),
                                slice=Slice(
                                    lower=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2, kind=None),
                                    ),
                                    upper=None,
                                    step=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='i', ctx=Store()),
                                    Name(id='digit', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='code', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='i', ctx=Load()),
                                            op=Mod(),
                                            right=Constant(value=2, kind=None),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='evensum', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='digit', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Name(id='oddsum', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='digit', ctx=Load())],
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
                            targets=[Name(id='total', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='evensum', ctx=Load()),
                                    op=Mult(),
                                    right=Constant(value=3, kind=None),
                                ),
                                op=Add(),
                                right=Name(id='oddsum', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value=10, kind=None),
                                    op=Sub(),
                                    right=BinOp(
                                        left=Name(id='total', ctx=Load()),
                                        op=Mod(),
                                        right=Constant(value=10, kind=None),
                                    ),
                                ),
                                op=Mod(),
                                right=Constant(value=10, kind=None),
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
                FunctionDef(
                    name='check_encoding',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='barcode', annotation=None, type_comment=None),
                            arg(arg='encoding', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Checks if the given barcode is correctly encoded.\n\n        :return: True if the barcode string is encoded with the provided encoding.\n        :rtype: bool\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='encoding', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='any', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='barcode_sizes', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='ean8', kind=None),
                                    Constant(value='ean13', kind=None),
                                    Constant(value='upca', kind=None),
                                ],
                                values=[
                                    Constant(value=8, kind=None),
                                    Constant(value=13, kind=None),
                                    Constant(value=12, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='barcode_size', ctx=Store())],
                            value=Subscript(
                                value=Name(id='barcode_sizes', ctx=Load()),
                                slice=Name(id='encoding', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='barcode', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='barcode_size', ctx=Load())],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='^\\d+$', kind=None),
                                            Name(id='barcode', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='get_barcode_check_digit',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='barcode', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='barcode', ctx=Load()),
                                                        slice=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
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
                FunctionDef(
                    name='sanitize_ean',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='ean', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns a valid zero padded EAN-13 from an EAN prefix.\n\n        :type ean: str\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ean', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='ean', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=0, kind=None),
                                            upper=Constant(value=13, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='zfill',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=13, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='ean', ctx=Load()),
                                    slice=Slice(
                                        lower=Constant(value=0, kind=None),
                                        upper=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='get_barcode_check_digit',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='ean', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
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
                FunctionDef(
                    name='sanitize_upc',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='upc', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns a valid zero padded UPC-A from a UPC-A prefix.\n\n        :type upc: str\n        ', kind=None),
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sanitize_ean',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        BinOp(
                                            left=Constant(value='0', kind=None),
                                            op=Add(),
                                            right=Name(id='upc', ctx=Load()),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Slice(
                                    lower=Constant(value=1, kind=None),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
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
                FunctionDef(
                    name='match_pattern',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='barcode', annotation=None, type_comment=None),
                            arg(arg='pattern', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Checks barcode matches the pattern and retrieves the optional numeric value in barcode.\n\n        :param barcode:\n        :type barcode: str\n        :param pattern:\n        :type pattern: str\n        :return: an object containing:\n            - value: the numerical value encoded in the barcode (0 if no value encoded)\n            - base_code: the barcode in which numerical content is replaced by 0's\n            - match: boolean\n        :rtype: dict\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='match', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='value', kind=None),
                                    Constant(value='base_code', kind=None),
                                    Constant(value='match', kind=None),
                                ],
                                values=[
                                    Constant(value=0, kind=None),
                                    Name(id='barcode', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='barcode', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='barcode', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='\\', kind=None),
                                                            Constant(value='\\\\', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='{', kind=None),
                                                    Constant(value='\\{', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='}', kind=None),
                                            Constant(value='\\}', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='.', kind=None),
                                    Constant(value='\\.', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='numerical_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='[{][N]*[D]*[}]', kind=None),
                                    Name(id='pattern', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='numerical_content', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='num_start', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='numerical_content', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='num_end', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='numerical_content', ctx=Load()),
                                            attr='end',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value_string', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='barcode', ctx=Load()),
                                        slice=Slice(
                                            lower=Name(id='num_start', ctx=Load()),
                                            upper=BinOp(
                                                left=Name(id='num_end', ctx=Load()),
                                                op=Sub(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='whole_part_match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='[{][N]*[D}]', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='numerical_content', ctx=Load()),
                                                    attr='group',
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
                                    targets=[Name(id='decimal_part_match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='[{N][D]*[}]', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='numerical_content', ctx=Load()),
                                                    attr='group',
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
                                    targets=[Name(id='whole_part', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='value_string', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='whole_part_match', ctx=Load()),
                                                        attr='end',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='decimal_part', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='0.', kind=None),
                                        op=Add(),
                                        right=Subscript(
                                            value=Name(id='value_string', ctx=Load()),
                                            slice=Slice(
                                                lower=Call(
                                                    func=Attribute(
                                                        value=Name(id='decimal_part_match', ctx=Load()),
                                                        attr='start',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                upper=BinOp(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Name(id='decimal_part_match', ctx=Load()),
                                                            attr='end',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='whole_part', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='whole_part', ctx=Store())],
                                            value=Constant(value='0', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='match', ctx=Load()),
                                            slice=Constant(value='value', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[Name(id='whole_part', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='float', ctx=Load()),
                                            args=[Name(id='decimal_part', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='match', ctx=Load()),
                                            slice=Constant(value='base_code', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Subscript(
                                                value=Name(id='barcode', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Name(id='num_start', ctx=Load()),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=Name(id='num_end', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(id='num_start', ctx=Load()),
                                                    ),
                                                    op=Sub(),
                                                    right=Constant(value=2, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Constant(value='0', kind=None),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Name(id='barcode', ctx=Load()),
                                            slice=Slice(
                                                lower=BinOp(
                                                    left=Name(id='num_end', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=2, kind=None),
                                                ),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='match', ctx=Load()),
                                            slice=Constant(value='base_code', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='match', ctx=Load()),
                                                                        slice=Constant(value='base_code', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='\\\\', kind=None),
                                                                    Constant(value='\\', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='\\{', kind=None),
                                                            Constant(value='{', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='\\}', kind=None),
                                                    Constant(value='}', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\.', kind=None),
                                            Constant(value='.', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pattern', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Subscript(
                                                value=Name(id='pattern', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Name(id='num_start', ctx=Load()),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=Name(id='num_end', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(id='num_start', ctx=Load()),
                                                    ),
                                                    op=Sub(),
                                                    right=Constant(value=2, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Constant(value='0', kind=None),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Name(id='pattern', ctx=Load()),
                                            slice=Slice(
                                                lower=Name(id='num_end', ctx=Load()),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='match', ctx=Load()),
                                    slice=Constant(value='match', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='pattern', ctx=Load()),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='match', ctx=Load()),
                                            slice=Constant(value='base_code', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='pattern', ctx=Load())],
                                                keywords=[],
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='match', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='parse_barcode',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='barcode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Attempts to interpret and parse a barcode.\n\n        :param barcode:\n        :type barcode: str\n        :return: A object containing various information about the barcode, like as:\n            - code: the barcode\n            - type: the barcode's type\n            - value: if the id encodes a numerical value, it will be put there\n            - base_code: the barcode code with all the encoding parts set to\n              zero; the one put on the product in the backend\n        :rtype: dict\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='parsed_result', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='encoding', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='code', kind=None),
                                    Constant(value='base_code', kind=None),
                                    Constant(value='value', kind=None),
                                ],
                                values=[
                                    Constant(value='', kind=None),
                                    Constant(value='error', kind=None),
                                    Name(id='barcode', ctx=Load()),
                                    Name(id='barcode', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rule', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='rule_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='cur_barcode', ctx=Store())],
                                    value=Name(id='barcode', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='encoding',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='ean13', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='check_encoding',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='barcode', ctx=Load()),
                                                    Constant(value='upca', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='upc_ean_conv',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='upc2ean', kind=None),
                                                            Constant(value='always', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='cur_barcode', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='0', kind=None),
                                                op=Add(),
                                                right=Name(id='cur_barcode', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='encoding',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='upca', kind=None)],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='check_encoding',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='barcode', ctx=Load()),
                                                            Constant(value='ean13', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='barcode', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='0', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='upc_ean_conv',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='ean2upc', kind=None),
                                                                    Constant(value='always', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='cur_barcode', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='cur_barcode', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Constant(value=1, kind=None),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='check_encoding',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='barcode', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='encoding',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='match_pattern',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cur_barcode', ctx=Load()),
                                            Attribute(
                                                value=Name(id='rule', ctx=Load()),
                                                attr='pattern',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='match', ctx=Load()),
                                        slice=Constant(value='match', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='alias', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='barcode', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='rule', ctx=Load()),
                                                        attr='alias',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='parsed_result', ctx=Load()),
                                                            slice=Constant(value='code', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='barcode', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='parsed_result', ctx=Load()),
                                                            slice=Constant(value='encoding', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='rule', ctx=Load()),
                                                        attr='encoding',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='parsed_result', ctx=Load()),
                                                            slice=Constant(value='type', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='rule', ctx=Load()),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='parsed_result', ctx=Load()),
                                                            slice=Constant(value='value', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='match', ctx=Load()),
                                                        slice=Constant(value='value', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='parsed_result', ctx=Load()),
                                                            slice=Constant(value='code', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='cur_barcode', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='encoding',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='ean13', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='parsed_result', ctx=Load()),
                                                                    slice=Constant(value='base_code', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sanitize_ean',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='match', ctx=Load()),
                                                                        slice=Constant(value='base_code', kind=None),
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
                                                                left=Attribute(
                                                                    value=Name(id='rule', ctx=Load()),
                                                                    attr='encoding',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='upca', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='parsed_result', ctx=Load()),
                                                                            slice=Constant(value='base_code', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='sanitize_upc',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='match', ctx=Load()),
                                                                                slice=Constant(value='base_code', kind=None),
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
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='parsed_result', ctx=Load()),
                                                                            slice=Constant(value='base_code', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Subscript(
                                                                        value=Name(id='match', ctx=Load()),
                                                                        slice=Constant(value='base_code', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                Return(
                                                    value=Name(id='parsed_result', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='parsed_result', ctx=Load()),
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
