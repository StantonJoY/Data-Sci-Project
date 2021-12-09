Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='itertools',
            names=[alias(name='groupby', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='populate', asname=None)],
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
        ClassDef(
            name='LunchProductCategory',
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
                    value=Constant(value='lunch.product.category', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_sizes', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='small', kind=None),
                            Constant(value='medium', kind=None),
                            Constant(value='large', kind=None),
                        ],
                        values=[
                            Constant(value=5, kind=None),
                            Constant(value=150, kind=None),
                            Constant(value=400, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[Constant(value='res.company', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            targets=[Name(id='company_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lunch_product_category_{counter}', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=List(
                                                            elts=[
                                                                Constant(value=False, kind=None),
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
                                                                        args=[Constant(value='base.main_company', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='company_ids', ctx=Load()),
                                                    ),
                                                    BinOp(
                                                        left=List(
                                                            elts=[
                                                                Constant(value=1, kind=None),
                                                                Constant(value=1, kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=BinOp(
                                                            left=List(
                                                                elts=[
                                                                    BinOp(
                                                                        left=Constant(value=2, kind=None),
                                                                        op=Div(),
                                                                        right=BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Call(
                                                                                    func=Name(id='len', ctx=Load()),
                                                                                    args=[Name(id='company_ids', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                Constant(value=1, kind=None),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            op=Mult(),
                                                            right=Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[Name(id='company_ids', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
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
            name='LunchProduct',
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
                    value=Constant(value='lunch.product', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_sizes', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='small', kind=None),
                            Constant(value='medium', kind=None),
                            Constant(value='large', kind=None),
                        ],
                        values=[
                            Constant(value=10, kind=None),
                            Constant(value=150, kind=None),
                            Constant(value=10000, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='lunch.product.category', kind=None),
                            Constant(value='lunch.supplier', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            targets=[Name(id='category_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='lunch.product.category', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='category_records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='lunch.product.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='category_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='category_by_company', ctx=Store())],
                            value=DictComp(
                                key=Name(id='k', ctx=Load()),
                                value=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[Name(id='v', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='k', ctx=Store()),
                                                Name(id='v', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Name(id='groupby', ctx=Load()),
                                            args=[Name(id='category_records', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='key',
                                                    value=Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='rec', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='rec', ctx=Load()),
                                                                slice=Constant(value='company_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='supplier_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='lunch.supplier', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_by_supplier', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='rec', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='rec', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='lunch.supplier', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='supplier_ids', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_category',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='random', annotation=None, type_comment=None),
                                    arg(arg='values', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company_id', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='company_by_supplier', ctx=Load()),
                                        slice=Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='supplier_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='random', ctx=Load()),
                                                attr='choice',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='category_by_company', ctx=Load()),
                                                    slice=Name(id='company_id', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='active', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lunch_product_{counter}', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='price', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randfloat',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=0.1, kind=None),
                                                    Constant(value=50, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='supplier_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='supplier_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='category_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_category', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
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
            name='LunchLocation',
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
                    value=Constant(value='lunch.location', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_sizes', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='small', kind=None),
                            Constant(value='medium', kind=None),
                            Constant(value='large', kind=None),
                        ],
                        values=[
                            Constant(value=3, kind=None),
                            Constant(value=50, kind=None),
                            Constant(value=500, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[Constant(value='res.company', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            targets=[Name(id='company_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lunch_location_{counter}', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='address', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lunch_address_location_{counter}', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='company_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
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
            name='LunchSupplier',
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
                    value=Constant(value='lunch.supplier', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_sizes', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='small', kind=None),
                            Constant(value='medium', kind=None),
                            Constant(value='large', kind=None),
                        ],
                        values=[
                            Constant(value=3, kind=None),
                            Constant(value=50, kind=None),
                            Constant(value=1500, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='lunch.location', kind=None),
                            Constant(value='res.partner', kind=None),
                            Constant(value='res.users', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            targets=[Name(id='location_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='lunch.location', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_location_ids',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='random', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='nb_locations', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='randint',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='location_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='random', ctx=Load()),
                                                            attr='choices',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='location_ids', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='k',
                                                                value=Name(id='nb_locations', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='active', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='send_by', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='phone', kind=None),
                                                            Constant(value='mail', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='delivery', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='delivery', kind=None),
                                                            Constant(value='no_delivery', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='mon', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='tue', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='wed', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='thu', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='fri', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sat', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sun', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='available_location_ids', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            List(elts=[], ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=6, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Name(id='location_ids', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='then',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='populate', ctx=Load()),
                                                                attr='compute',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='get_location_ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='partner_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='partner_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='responsible_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='user_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='moment', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='am', kind=None),
                                                            Constant(value='pm', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='automatic_email_time', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randfloat',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=12, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
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
            name='LunchOrder',
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
                    value=Constant(value='lunch.order', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_sizes', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='small', kind=None),
                            Constant(value='medium', kind=None),
                            Constant(value='large', kind=None),
                        ],
                        values=[
                            Constant(value=20, kind=None),
                            Constant(value=3000, kind=None),
                            Constant(value=15000, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='lunch.product', kind=None),
                            Constant(value='res.users', kind=None),
                            Constant(value='res.company', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='lunch.product', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='active', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='new', kind=None),
                                                            Constant(value='confirmed', kind=None),
                                                            Constant(value='ordered', kind=None),
                                                            Constant(value='cancelled', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='product_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='product_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='user_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='user_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='note', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lunch_note_{counter}', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='company_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='quantity', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randint',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
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
            name='LunchAlert',
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
                    value=Constant(value='lunch.alert', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_sizes', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='small', kind=None),
                            Constant(value='medium', kind=None),
                            Constant(value='large', kind=None),
                        ],
                        values=[
                            Constant(value=10, kind=None),
                            Constant(value=40, kind=None),
                            Constant(value=150, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[Constant(value='lunch.location', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            targets=[Name(id='location_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='lunch.location', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_location_ids',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='random', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='nb_max', ctx=Store())],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='location_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='start', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='randint',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Name(id='nb_max', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='end', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='randint',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='start', ctx=Load()),
                                            Name(id='nb_max', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='location_ids', ctx=Load()),
                                        slice=Slice(
                                            lower=Name(id='start', ctx=Load()),
                                            upper=Name(id='end', ctx=Load()),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='active', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='recipients', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='everyone', kind=None),
                                                            Constant(value='last_week', kind=None),
                                                            Constant(value='last_month', kind=None),
                                                            Constant(value='last_year', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='mode', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='alert', kind=None),
                                                            Constant(value='chat', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='mon', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='tue', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='wed', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='thu', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='fri', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sat', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sun', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.9, kind=None),
                                                            Constant(value=0.1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='alert_{counter}', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='message', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='<strong>alert message {counter}</strong>', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='notification_time', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randfloat',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=12, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='notification_moment', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='am', kind=None),
                                                            Constant(value='pm', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='until', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randdatetime',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='relative_before',
                                                        value=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='years',
                                                                    value=UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=2, kind=None),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='relative_after',
                                                        value=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='years',
                                                                    value=Constant(value=2, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='location_ids', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_location_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
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
