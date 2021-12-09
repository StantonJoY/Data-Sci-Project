Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='xlrd', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='pycompat', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='_is_true',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='s', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Compare(
                        left=Name(id='s', ctx=Load()),
                        ops=[NotIn()],
                        comparators=[
                            Tuple(
                                elts=[
                                    Constant(value='F', kind=None),
                                    Constant(value='False', kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value=None, kind=None),
                                    Constant(value=False, kind=None),
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
        ClassDef(
            name='LuxTaxGenerator',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='workbook',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xlrd', ctx=Load()),
                                    attr='open_workbook',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tax.xls', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sheet_info',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='workbook',
                                        ctx=Load(),
                                    ),
                                    attr='sheet_by_name',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='INFO', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sheet_taxes',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='workbook',
                                        ctx=Load(),
                                    ),
                                    attr='sheet_by_name',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='TAXES', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sheet_tax_codes',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='workbook',
                                        ctx=Load(),
                                    ),
                                    attr='sheet_by_name',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='TAX.CODES', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sheet_fiscal_pos_map',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='workbook',
                                        ctx=Load(),
                                    ),
                                    attr='sheet_by_name',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='FISCAL.POSITION.MAPPINGS', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='suffix',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sheet_info',
                                        ctx=Load(),
                                    ),
                                    attr='cell_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=4, kind=None),
                                    Constant(value=2, kind=None),
                                ],
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
                    name='iter_tax_codes',
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
                            targets=[Name(id='keys', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='c', ctx=Load()),
                                    attr='value',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='c', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sheet_tax_codes',
                                                    ctx=Load(),
                                                ),
                                                attr='row',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Yield(
                                value=Name(id='keys', ctx=Load()),
                            ),
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=1, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sheet_tax_codes',
                                            ctx=Load(),
                                        ),
                                        attr='nrows',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='row', ctx=Store())],
                                    value=GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='c', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sheet_tax_codes',
                                                            ctx=Load(),
                                                        ),
                                                        attr='row',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='i', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='d', ctx=Store())],
                                    value=Call(
                                        func=Name(id='OrderedDict', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='zip', ctx=Load()),
                                                args=[
                                                    Name(id='keys', ctx=Load()),
                                                    Name(id='row', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='d', ctx=Load()),
                                            slice=Constant(value='sign', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='d', ctx=Load()),
                                                slice=Constant(value='sign', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='d', ctx=Load()),
                                            slice=Constant(value='sequence', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='d', ctx=Load()),
                                                slice=Constant(value='sequence', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(
                                        value=Name(id='d', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='iter_taxes',
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
                            targets=[Name(id='keys', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='c', ctx=Load()),
                                    attr='value',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='c', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sheet_taxes',
                                                    ctx=Load(),
                                                ),
                                                attr='row',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Yield(
                                value=Name(id='keys', ctx=Load()),
                            ),
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=1, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sheet_taxes',
                                            ctx=Load(),
                                        ),
                                        attr='nrows',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='row', ctx=Store())],
                                    value=GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='c', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sheet_taxes',
                                                            ctx=Load(),
                                                        ),
                                                        attr='row',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='i', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(
                                        value=Call(
                                            func=Name(id='OrderedDict', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='zip', ctx=Load()),
                                                    args=[
                                                        Name(id='keys', ctx=Load()),
                                                        Name(id='row', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='iter_fiscal_pos_map',
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
                            targets=[Name(id='keys', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='c', ctx=Load()),
                                    attr='value',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='c', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sheet_fiscal_pos_map',
                                                    ctx=Load(),
                                                ),
                                                attr='row',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Yield(
                                value=Name(id='keys', ctx=Load()),
                            ),
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=1, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sheet_fiscal_pos_map',
                                            ctx=Load(),
                                        ),
                                        attr='nrows',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='row', ctx=Store())],
                                    value=GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='c', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sheet_fiscal_pos_map',
                                                            ctx=Load(),
                                                        ),
                                                        attr='row',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='i', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(
                                        value=Call(
                                            func=Name(id='OrderedDict', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='zip', ctx=Load()),
                                                    args=[
                                                        Name(id='keys', ctx=Load()),
                                                        Name(id='row', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='tax_codes_to_csv',
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
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_writer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='account.tax.code.template-%s.csv', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='suffix',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='wb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_codes_iterator', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='iter_tax_codes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='keys', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[Name(id='tax_codes_iterator', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='writerow',
                                    ctx=Load(),
                                ),
                                args=[Name(id='keys', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tax_codes', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Name(id='tax_codes_iterator', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='tax_code', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='row', ctx=Load()),
                                        slice=Constant(value='code', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='tax_code', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='tax_codes', ctx=Load())],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='RuntimeError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='duplicate tax code %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='tax_code', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='tax_codes', ctx=Load()),
                                            slice=Name(id='tax_code', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='row', ctx=Load()),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='writerow',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='pycompat', ctx=Load()),
                                                        attr='to_text',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='v', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='v', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='row', ctx=Load()),
                                                                attr='values',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_tax_codes', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='add_new_tax_code',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='tax_code_id', annotation=None, type_comment=None),
                                    arg(arg='new_name', annotation=None, type_comment=None),
                                    arg(arg='new_parent_code', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='tax_code_id', ctx=Load()),
                                    ),
                                    body=[Return(value=None)],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='name', ctx=Store()),
                                                Name(id='parent_code', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='new_tax_codes', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tax_code_id', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
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
                                        op=And(),
                                        values=[
                                            Name(id='parent_code', ctx=Load()),
                                            Compare(
                                                left=Name(id='parent_code', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='new_parent_code', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='RuntimeError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='tax code "%s" already exist with parent %s while trying to add it with parent %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='tax_code_id', ctx=Load()),
                                                                Name(id='parent_code', ctx=Load()),
                                                                Name(id='new_parent_code', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='new_tax_codes', ctx=Load()),
                                                    slice=Name(id='tax_code_id', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='new_name', ctx=Load()),
                                                    Name(id='new_parent_code', ctx=Load()),
                                                ],
                                                ctx=Load(),
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
                        Assign(
                            targets=[Name(id='taxes_iterator', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='iter_taxes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[Name(id='taxes_iterator', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Name(id='taxes_iterator', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='_is_true', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='active', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='child_depend', kind=None),
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='amount', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='RuntimeError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='amount must be one if child_depend for %s', kind=None),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value='id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='base_code', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='row', ctx=Load()),
                                        slice=Constant(value='BASE_CODE', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='base_code', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Name(id='base_code', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='/', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='base_code', ctx=Store())],
                                            value=Constant(value='NA', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='base_code', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='tax_codes', ctx=Load())],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='RuntimeError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='undefined tax code %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='base_code', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='base_code', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='NA', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='child_depend', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='RuntimeError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='base code specified with child_depend for %s', kind=None),
                                                                op=Mod(),
                                                                right=Subscript(
                                                                    value=Name(id='row', ctx=Load()),
                                                                    slice=Constant(value='id', kind=None),
                                                                    ctx=Load(),
                                                                ),
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
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='row', ctx=Load()),
                                            slice=Constant(value='child_depend', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='base_code', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='NA', kind=None)],
                                            ),
                                            body=[
                                                Assert(
                                                    test=Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='base_code_id:id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    msg=BinOp(
                                                        left=Constant(value='missing base_code_id for %s', kind=None),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value='id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assert(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='ref_base_code_id:id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='base_code_id:id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            msg=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='add_new_tax_code', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='base_code_id:id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='Base - ', kind=None),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='base_code', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='tax_code', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='row', ctx=Load()),
                                        slice=Constant(value='TAX_CODE', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='tax_code', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Name(id='tax_code', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='/', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='tax_code', ctx=Store())],
                                            value=Constant(value='NA', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='tax_code', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='tax_codes', ctx=Load())],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='RuntimeError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='undefined tax code %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='tax_code', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='tax_code', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='NA', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='amount', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value='child_depend', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='RuntimeError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='TAX_CODE not specified for non-zero tax %s', kind=None),
                                                                op=Mod(),
                                                                right=Subscript(
                                                                    value=Name(id='row', ctx=Load()),
                                                                    slice=Constant(value='id', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='tax_code_id:id', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='RuntimeError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='tax_code_id specified for tax %s', kind=None),
                                                                op=Mod(),
                                                                right=Subscript(
                                                                    value=Name(id='row', ctx=Load()),
                                                                    slice=Constant(value='id', kind=None),
                                                                    ctx=Load(),
                                                                ),
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
                                    orelse=[
                                        If(
                                            test=Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='child_depend', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='RuntimeError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='TAX_CODE specified with child_depend for %s', kind=None),
                                                                op=Mod(),
                                                                right=Subscript(
                                                                    value=Name(id='row', ctx=Load()),
                                                                    slice=Constant(value='id', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='amount', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='RuntimeError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='TAX_CODE specified for zero tax %s', kind=None),
                                                                op=Mod(),
                                                                right=Subscript(
                                                                    value=Name(id='row', ctx=Load()),
                                                                    slice=Constant(value='id', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='tax_code_id:id', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='RuntimeError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='tax_code_id not specified for tax %s', kind=None),
                                                                op=Mod(),
                                                                right=Subscript(
                                                                    value=Name(id='row', ctx=Load()),
                                                                    slice=Constant(value='id', kind=None),
                                                                    ctx=Load(),
                                                                ),
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
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='child_depend', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='amount', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assert(
                                            test=Subscript(
                                                value=Name(id='row', ctx=Load()),
                                                slice=Constant(value='tax_code_id:id', kind=None),
                                                ctx=Load(),
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='missing tax_code_id for %s', kind=None),
                                                op=Mod(),
                                                right=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='id', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                        Assert(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='ref_tax_code_id:id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='tax_code_id:id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            msg=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='add_new_tax_code', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='tax_code_id:id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='Taxe - ', kind=None),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='tax_code', ctx=Load()),
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
                        For(
                            target=Name(id='tax_code_id', ctx=Store()),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[Name(id='new_tax_codes', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='name', ctx=Store()),
                                                Name(id='parent_code', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='new_tax_codes', ctx=Load()),
                                        slice=Name(id='tax_code_id', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='writerow',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='tax_code_id', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='lu_tct_m', kind='u'),
                                                        op=Add(),
                                                        right=Name(id='parent_code', ctx=Load()),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='tax_code_id', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='lu_tax_code_template_', kind=None),
                                                            Constant(value='', kind='u'),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='1', kind='u'),
                                                    Constant(value='', kind='u'),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='pycompat', ctx=Load()),
                                                            attr='to_text',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='', kind='u'),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='taxes_to_csv',
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
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_writer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='account.tax.template-%s.csv', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='suffix',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='wb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='taxes_iterator', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='iter_taxes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='keys', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[Name(id='taxes_iterator', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='writerow',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Subscript(
                                            value=Name(id='keys', ctx=Load()),
                                            slice=Slice(
                                                lower=Constant(value=3, kind=None),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=List(
                                            elts=[Constant(value='sequence', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='seq', ctx=Store())],
                            value=Constant(value=100, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[Name(id='taxes_iterator', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='r', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=Name(id='r', ctx=Load()),
                                                slice=Constant(value='description', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='_is_true', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value='active', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Name(id='seq', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                If(
                                    test=Subscript(
                                        value=Name(id='row', ctx=Load()),
                                        slice=Constant(value='parent_id:id', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='cur_seq', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='seq', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1000, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='cur_seq', ctx=Store())],
                                            value=Name(id='seq', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='writerow',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=ListComp(
                                                    elt=Call(
                                                        func=Attribute(
                                                            value=Name(id='pycompat', ctx=Load()),
                                                            attr='to_text',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='v', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='v', ctx=Store()),
                                                            iter=Subscript(
                                                                value=Call(
                                                                    func=Name(id='list', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='row', ctx=Load()),
                                                                                attr='values',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                slice=Slice(
                                                                    lower=Constant(value=3, kind=None),
                                                                    upper=None,
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                                op=Add(),
                                                right=List(
                                                    elts=[Name(id='cur_seq', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fiscal_pos_map_to_csv',
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
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='csv_writer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='account.fiscal.position.tax.template-%s.csv', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='suffix',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value='wb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fiscal_pos_map_iterator', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='iter_fiscal_pos_map',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='keys', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[Name(id='fiscal_pos_map_iterator', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='writerow',
                                    ctx=Load(),
                                ),
                                args=[Name(id='keys', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Name(id='fiscal_pos_map_iterator', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='writerow',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='pycompat', ctx=Load()),
                                                        attr='to_text',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='s', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='s', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='row', ctx=Load()),
                                                                attr='values',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
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
                            orelse=[],
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
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='o', ctx=Store())],
                    value=Call(
                        func=Name(id='LuxTaxGenerator', ctx=Load()),
                        args=[Constant(value='tax.xls', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='o', ctx=Load()),
                            attr='tax_codes_to_csv',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='o', ctx=Load()),
                            attr='taxes_to_csv',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='o', ctx=Load()),
                            attr='fiscal_pos_map_to_csv',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
