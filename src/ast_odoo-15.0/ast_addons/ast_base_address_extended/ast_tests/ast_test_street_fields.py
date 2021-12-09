Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestStreetFields',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                            Name(id='TestStreetFields', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='Partner',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.be', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='street_format', kind=None)],
                                        values=[Constant(value='%(street_name)s, %(street_number)s/%(street_number2)s', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.us', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='street_format', kind=None)],
                                        values=[Constant(value='%(street_number)s/%(street_number2)s %(street_name)s', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.ch', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='street_format', kind=None)],
                                        values=[Constant(value='header %(street_name)s, %(street_number)s - %(street_number2)s trailer', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.mx', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='street_format', kind=None)],
                                        values=[Constant(value='%(street_name)s %(street_number)s/%(street_number2)s', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertStreetVals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='street_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='val', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='street_data', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='key', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='street', kind=None),
                                                    Constant(value='street_name', kind=None),
                                                    Constant(value='street_number', kind=None),
                                                    Constant(value='street_number2', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='city', kind=None),
                                                    Constant(value='country_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Name(id='key', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='models', ctx=Load()),
                                                attr='BaseModel',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='record', ctx=Load()),
                                                            slice=Name(id='key', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='val', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='Wrongly formatted street field %s: expected %s, received %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='key', ctx=Load()),
                                                                Name(id='val', ctx=Load()),
                                                                Subscript(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    slice=Name(id='key', ctx=Load()),
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
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=Name(id='key', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='val', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='Wrongly formatted street field %s: expected %s, received %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='key', ctx=Load()),
                                                                Name(id='val', ctx=Load()),
                                                                Subscript(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    slice=Name(id='key', ctx=Load()),
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_company_create',
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
                            value=Constant(value=' Will test the compute and inverse methods of street fields when creating partner records. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='us_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.us', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mx_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.mx', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ch_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.ch', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='input_values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='us_id', ctx=Load()),
                                            Constant(value='40/2b Chaussee de Namur', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='us_id', ctx=Load()),
                                            Constant(value='40 Chaussee de Namur', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='us_id', ctx=Load()),
                                            Constant(value='Chaussee de Namur', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='mx_id', ctx=Load()),
                                            Constant(value='Av. Miguel Hidalgo y Costilla 601', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='mx_id', ctx=Load()),
                                            Constant(value='Av. Miguel Hidalgo y Costilla 601/40', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='ch_id', ctx=Load()),
                                            Constant(value='header Chaussee de Namur, 40 - 2b trailer', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='ch_id', ctx=Load()),
                                            Constant(value='header Chaussee de Namur, 40 trailer', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='ch_id', ctx=Load()),
                                            Constant(value='header Chaussee de Namur trailer', kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='2b', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='de Namur', kind=None),
                                            Constant(value='Chaussee', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Av. Miguel Hidalgo y Costilla', kind=None),
                                            Constant(value='601', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Av. Miguel Hidalgo y Costilla', kind=None),
                                            Constant(value='601', kind=None),
                                            Constant(value='40', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='2b', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='idx', ctx=Store()),
                                    Tuple(
                                        elts=[
                                            Name(id='company_values', ctx=Store()),
                                            Name(id='expected_vals', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Name(id='input_values', ctx=Load()),
                                            Name(id='expected', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='company_values', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='Test-%2d', kind=None),
                                        op=Mod(),
                                        right=Name(id='idx', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='company_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertStreetVals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='company', ctx=Load()),
                                            Name(id='expected_vals', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertStreetVals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            Name(id='expected_vals', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='idx', ctx=Store()),
                                    Tuple(
                                        elts=[
                                            Name(id='company_values', ctx=Store()),
                                            Name(id='expected_vals', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Name(id='input_values', ctx=Load()),
                                            Name(id='expected', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='company_values', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='TestNew-%2d', kind=None),
                                        op=Mod(),
                                        right=Name(id='idx', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='expected_street', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='company_values', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='street', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='company_values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='expected_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='company_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='street',
                                                ctx=Load(),
                                            ),
                                            Name(id='expected_street', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertStreetVals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='company', ctx=Load()),
                                            Name(id='company_values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='street',
                                                ctx=Load(),
                                            ),
                                            Name(id='expected_street', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertStreetVals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            Name(id='company_values', ctx=Load()),
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
                    name='test_company_write',
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
                            value=Constant(value=' Will test the compute and inverse methods of street fields when updating partner records. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='be_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.be', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test', kind=None),
                                            Name(id='be_id', ctx=Load()),
                                            Constant(value='Chaussee de Namur, 40/2b', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertStreetVals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='company', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='2b', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='input_values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[Constant(value='street', kind=None)],
                                        values=[Constant(value='Chaussee de Namur, 43', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='street', kind=None)],
                                        values=[Constant(value='Chaussee de Namur', kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[Constant(value='street_number2', kind=None)],
                                        values=[Constant(value='4', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='country_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.us', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='43', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='Chee de Namur, 40', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='4', kind=None),
                                            Constant(value='Chee de Namur, 40/4', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='4', kind=None),
                                            Constant(value='40/4 Chee de Namur', kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='write_values', ctx=Store()),
                                    Name(id='expected_vals', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='input_values', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='write_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertStreetVals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='company', ctx=Load()),
                                            Name(id='expected_vals', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertStreetVals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            Name(id='expected_vals', ctx=Load()),
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
                    name='test_partner_create',
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
                            value=Constant(value=' Will test the compute and inverse methods of street fields when creating partner records. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='us_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.us', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mx_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.mx', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ch_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.ch', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='input_values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='us_id', ctx=Load()),
                                            Constant(value='40/2b Chaussee de Namur', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='us_id', ctx=Load()),
                                            Constant(value='40 Chaussee de Namur', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='us_id', ctx=Load()),
                                            Constant(value='Chaussee de Namur', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='mx_id', ctx=Load()),
                                            Constant(value='Av. Miguel Hidalgo y Costilla 601', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='mx_id', ctx=Load()),
                                            Constant(value='Av. Miguel Hidalgo y Costilla 601/40', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='ch_id', ctx=Load()),
                                            Constant(value='header Chaussee de Namur, 40 - 2b trailer', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='ch_id', ctx=Load()),
                                            Constant(value='header Chaussee de Namur, 40 trailer', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Name(id='ch_id', ctx=Load()),
                                            Constant(value='header Chaussee de Namur trailer', kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='2b', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='de Namur', kind=None),
                                            Constant(value='Chaussee', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Av. Miguel Hidalgo y Costilla', kind=None),
                                            Constant(value='601', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Av. Miguel Hidalgo y Costilla', kind=None),
                                            Constant(value='601', kind=None),
                                            Constant(value='40', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='2b', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='partner_values', ctx=Store()),
                                    Name(id='expected_vals', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='input_values', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='partner_values', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Test', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertStreetVals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='partner', ctx=Load()),
                                            Name(id='expected_vals', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='partner_values', ctx=Store()),
                                    Name(id='expected_vals', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='input_values', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='partner_values', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Test', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='expected_street', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partner_values', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='street', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partner_values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='expected_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='street',
                                                ctx=Load(),
                                            ),
                                            Name(id='expected_street', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertStreetVals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='partner', ctx=Load()),
                                            Name(id='partner_values', ctx=Load()),
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
                    name='test_partner_write',
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
                            value=Constant(value=' Will test the compute and inverse methods of street fields when updating partner records. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='be_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.be', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test', kind=None),
                                            Name(id='be_id', ctx=Load()),
                                            Constant(value='Chaussee de Namur, 40/2b', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertStreetVals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='partner', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='2b', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='input_values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[Constant(value='street', kind=None)],
                                        values=[Constant(value='Chaussee de Namur, 43', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='street', kind=None)],
                                        values=[Constant(value='Chaussee de Namur', kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[Constant(value='street_number2', kind=None)],
                                        values=[Constant(value='4', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='country_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.us', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value='43', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chaussee de Namur', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='Chee de Namur, 40', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='4', kind=None),
                                            Constant(value='Chee de Namur, 40/4', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='street_name', kind=None),
                                            Constant(value='street_number', kind=None),
                                            Constant(value='street_number2', kind=None),
                                            Constant(value='street', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Chee de Namur', kind=None),
                                            Constant(value='40', kind=None),
                                            Constant(value='4', kind=None),
                                            Constant(value='40/4 Chee de Namur', kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='write_values', ctx=Store()),
                                    Name(id='expected_vals', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='input_values', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='write_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertStreetVals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='partner', ctx=Load()),
                                            Name(id='expected_vals', ctx=Load()),
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
    ],
    type_ignores=[],
)
