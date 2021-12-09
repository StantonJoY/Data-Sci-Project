Module(
    body=[
        Import(
            names=[alias(name='collections', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
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
            name='Partner',
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
                    value=Constant(value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='res.company', kind=None),
                            Constant(value='res.partner.industry', kind=None),
                        ],
                        ctx=Load(),
                    ),
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
                            Constant(value=100, kind=None),
                            Constant(value=2000, kind=None),
                            Constant(value=100000, kind=None),
                        ],
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
                            targets=[Name(id='address_factories_groups', ctx=Store())],
                            value=List(
                                elts=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='street', kind=None),
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
                                                                    Constant(value='', kind=None),
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
                                                    Constant(value='street2', kind=None),
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
                                                                    Constant(value='', kind=None),
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
                                                    Constant(value='city', kind=None),
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
                                                                    Constant(value='', kind=None),
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
                                                    Constant(value='zip', kind=None),
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
                                                                    Constant(value='', kind=None),
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
                                                    Constant(value='country_id', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[Constant(value=False, kind=None)],
                                                                ctx=Load(),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='street', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[Constant(value='Boulevard Tintin {counter}', kind=None)],
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
                                                    Constant(value='city', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[Constant(value='Brussels', kind=None)],
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
                                                    Constant(value='zip', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[Constant(value=1020, kind=None)],
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
                                                    Constant(value='country_id', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
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
                                                                            args=[Constant(value='base.be', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='street', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='Main street', kind=None),
                                                                    Constant(value='3th street {counter}', kind=None),
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
                                                    Constant(value='street2', kind=None),
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
                                                                    Constant(value='', kind=None),
                                                                    Constant(value='Behind the tree {counter}', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value=90, kind=None),
                                                                    Constant(value=5, kind=None),
                                                                    Constant(value=5, kind=None),
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
                                                    Constant(value='city', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='randomize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='Sans Fransisco', kind=None),
                                                                    Constant(value='Los Angeles', kind=None),
                                                                    Constant(value='', kind=None),
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
                                                    Constant(value='zip', kind=None),
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
                                                                    Constant(value='', kind=None),
                                                                    Constant(value='50231', kind=None),
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
                                                    Constant(value='country_id', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
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
                                                                ctx=Load(),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='street', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='Main Street', kind=None),
                                                                    Constant(value='Some Street {counter}', kind=None),
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
                                                    Constant(value='city', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[Constant(value='ગાંધીનગર (Gandhinagar)', kind=None)],
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
                                                    Constant(value='zip', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='randomize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='382002', kind=None),
                                                                    Constant(value='382008', kind=None),
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
                                                    Constant(value='country_id', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='randomize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
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
                                                                            args=[Constant(value='base.in', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='street', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='万泉寺村', kind=None),
                                                                    Constant(value='საბჭოს სკვერი {counter}', kind=None),
                                                                    Constant(value='10th Street {counter}', kind=None),
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
                                                    Constant(value='city', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='iterate',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='北京市', kind=None),
                                                                    Constant(value='თბილისი', kind=None),
                                                                    Constant(value='دبي', kind=None),
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
                                                    Constant(value='zip', kind=None),
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
                                                                    Constant(value='UF47', kind=None),
                                                                    Constant(value='0', kind=None),
                                                                    Constant(value='10201', kind=None),
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
                                                    Constant(value='country_id', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='populate', ctx=Load()),
                                                            attr='randomize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=List(
                                                                    elts=[Constant(value=False, kind=None)],
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='res.country', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='search',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[List(elts=[], ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='ids',
                                                                    ctx=Load(),
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
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='generate_address',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='iterator', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='address_generators', ctx=Store())],
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='populate', ctx=Load()),
                                                attr='chain_factories',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='address_factories', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='address_factories', ctx=Store()),
                                                iter=Name(id='address_factories_groups', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='adress_generator', ctx=Store()),
                                    iter=Name(id='address_generators', ctx=Load()),
                                    body=[
                                        For(
                                            target=Name(id='adress_values', ctx=Store()),
                                            iter=Name(id='adress_generator', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Subscript(
                                                        value=Name(id='adress_values', ctx=Load()),
                                                        slice=Constant(value='__complete', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='values', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='next', ctx=Load()),
                                                        args=[Name(id='iterator', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Yield(
                                                        value=Dict(
                                                            keys=[
                                                                None,
                                                                None,
                                                            ],
                                                            values=[
                                                                Name(id='values', ctx=Load()),
                                                                Name(id='adress_values', ctx=Load()),
                                                            ],
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='r', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='populate', ctx=Load()),
                                            attr='Random',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='res.partner+address_generator_selector', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='values', ctx=Store()),
                                    iter=Name(id='iterator', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='adress_generator', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='r', ctx=Load()),
                                                    attr='choice',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='address_generators', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='adress_values', ctx=Store())],
                                            value=Call(
                                                func=Name(id='next', ctx=Load()),
                                                args=[Name(id='adress_generator', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Yield(
                                                value=Dict(
                                                    keys=[
                                                        None,
                                                        None,
                                                    ],
                                                    values=[
                                                        Name(id='adress_values', ctx=Load()),
                                                        Name(id='values', ctx=Load()),
                                                    ],
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
                        Assign(
                            targets=[Name(id='states', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.country.state', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='states_per_country', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='collections', ctx=Load()),
                                    attr='defaultdict',
                                    ctx=Load(),
                                ),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='state', ctx=Store()),
                            iter=Name(id='states', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='states_per_country', ctx=Load()),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='state', ctx=Load()),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='state', ctx=Load()),
                                                attr='id',
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
                        FunctionDef(
                            name='get_state',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='values', annotation=None, type_comment=None),
                                    arg(arg='random', annotation=None, type_comment=None),
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
                                    targets=[Name(id='country_id', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='country_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='country_id', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='choice',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=List(
                                                    elts=[Constant(value=False, kind=None)],
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='states_per_country', ctx=Load()),
                                                    slice=Name(id='country_id', ctx=Load()),
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
                            name='get_name',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='values', annotation=None, type_comment=None),
                                    arg(arg='counter', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[
                                    Constant(value=None, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='is_company', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='is_company', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='complete', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='__complete', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=BinOp(
                                        left=Constant(value='%s_%s_%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                IfExp(
                                                    test=Name(id='is_company', ctx=Load()),
                                                    body=Constant(value='company', kind=None),
                                                    orelse=Constant(value='partner', kind=None),
                                                ),
                                                Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='complete', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Name(id='counter', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='industry_ids', ctx=Store())],
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
                                slice=Constant(value='res.partner.industry', kind=None),
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
                                            Constant(value='employee', kind=None),
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
                                                    List(
                                                        elts=[
                                                            Constant(value=0.1, kind=None),
                                                            Constant(value=0.9, kind=None),
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
                                            Constant(value='email', kind=None),
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
                                                            Constant(value='', kind=None),
                                                            Constant(value='email{counter}@example.com', kind=None),
                                                            Constant(value='<contact 万> contact{counter}@anotherexample.com', kind=None),
                                                            Constant(value='invalid_email', kind=None),
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
                                            Constant(value='type', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='contact', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='is_company', kind=None),
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
                                                            Constant(value=0.05, kind=None),
                                                            Constant(value=0.95, kind=None),
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
                                            Constant(value='_address', kind=None),
                                            Name(id='generate_address', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_state', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='phone', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='', kind=None),
                                                            Constant(value='+3212345678', kind=None),
                                                            Constant(value='003212345678', kind=None),
                                                            Constant(value='12345678', kind=None),
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
                                            Constant(value='mobile', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='', kind=None),
                                                            Constant(value='+32412345678', kind=None),
                                                            Constant(value='0032412345678', kind=None),
                                                            Constant(value='412345678', kind=None),
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
                                            Constant(value='title', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='res.partner.title', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='search',
                                                                ctx=Load(),
                                                            ),
                                                            args=[List(elts=[], ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='ids',
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
                                            Constant(value='function', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='', kind=None),
                                                            Constant(value='President of Sales', kind=None),
                                                            Constant(value='Senior Consultant', kind=None),
                                                            Constant(value='Product owner', kind=None),
                                                            Constant(value='Functional Consultant', kind=None),
                                                            Constant(value='Chief Executive Officer', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=50, kind=None),
                                                            Constant(value=10, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value=20, kind=None),
                                                            Constant(value=5, kind=None),
                                                            Constant(value=10, kind=None),
                                                            Constant(value=1, kind=None),
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
                                            Constant(value='tz', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    ListComp(
                                                        elt=Name(id='tz', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='tz', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='env',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value='res.partner', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='_fields',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='tz', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='get_values',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
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
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='website', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='', kind=None),
                                                            Constant(value='http://www.example.com', kind=None),
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
                                            Constant(value='credit_limit', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=500, kind=None),
                                                            Constant(value=2500, kind=None),
                                                            Constant(value=5000, kind=None),
                                                            Constant(value=10000, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=50, kind=None),
                                                            Constant(value=30, kind=None),
                                                            Constant(value=5, kind=None),
                                                            Constant(value=5, kind=None),
                                                            Constant(value=5, kind=None),
                                                            Constant(value=5, kind=None),
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
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='ref', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='', kind=None),
                                                            Constant(value='{counter}', kind=None),
                                                            Constant(value='p-{counter}', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=10, kind=None),
                                                            Constant(value=10, kind=None),
                                                            Constant(value=30, kind=None),
                                                            Constant(value=50, kind=None),
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
                                            Constant(value='industry_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=List(
                                                            elts=[Constant(value=False, kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='industry_ids', ctx=Load()),
                                                    ),
                                                    BinOp(
                                                        left=List(
                                                            elts=[Constant(value=0.5, kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=BinOp(
                                                            left=List(
                                                                elts=[
                                                                    BinOp(
                                                                        left=Constant(value=0.5, kind=None),
                                                                        op=Div(),
                                                                        right=BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Call(
                                                                                    func=Name(id='len', ctx=Load()),
                                                                                    args=[Name(id='industry_ids', ctx=Load())],
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
                                                                args=[Name(id='industry_ids', ctx=Load())],
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
                                    Tuple(
                                        elts=[
                                            Constant(value='comment', kind=None),
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
                                                            Constant(value='', kind=None),
                                                            Constant(value='This is a partner {counter}', kind=None),
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
                                                                        left=Constant(value=1, kind=None),
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
                                    Tuple(
                                        elts=[
                                            Constant(value='parent_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=False, kind=None)],
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
                FunctionDef(
                    name='_populate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_populate',
                                    ctx=Load(),
                                ),
                                args=[Name(id='size', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_populate_set_companies',
                                    ctx=Load(),
                                ),
                                args=[Name(id='records', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='records', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_set_companies',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Setting companies', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='r_company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='populate', ctx=Load()),
                                    attr='Random',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='res.partner+company_has_partners', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='populate', ctx=Load()),
                                    attr='Random',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='res.partner+partner_has_company', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r_company_pick', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='populate', ctx=Load()),
                                    attr='Random',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='res.partner+partner_company_pick=', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='companies', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='records', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='is_company',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='r_company', ctx=Load()),
                                                        attr='getrandbits',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=1, kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='records', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='is_company',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='r_partner', ctx=Load()),
                                                        attr='getrandbits',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=1, kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='companies_partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='collections', ctx=Load()),
                                    attr='defaultdict',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.partner', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='partners', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='companies_partners', ctx=Load()),
                                        slice=Call(
                                            func=Attribute(
                                                value=Name(id='r_company_pick', ctx=Load()),
                                                attr='choice',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='companies', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Name(id='partner', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='count', ctx=Store()),
                                    Tuple(
                                        elts=[
                                            Name(id='company', ctx=Store()),
                                            Name(id='partners', ctx=Store()),
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
                                        func=Attribute(
                                            value=Name(id='companies_partners', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='start',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='count', ctx=Load()),
                                            op=Mod(),
                                            right=Constant(value=100, kind=None),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Setting company: %s/%s', kind=None),
                                                    Name(id='count', ctx=Load()),
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='companies', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partners', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='parent_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partners', ctx=Load()),
                                            attr='_onchange_company_id',
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ResPartnerIndustry',
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
                    value=Constant(value='res.partner.industry', kind=None),
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
                            Constant(value=15, kind=None),
                            Constant(value=60, kind=None),
                            Constant(value=300, kind=None),
                        ],
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
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.1, kind=None),
                                                            Constant(value=0.9, kind=None),
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
                                                    attr='cartesian',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='Industry name', kind=None),
                                                            Constant(value='Industry name {counter}', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.08, kind=None),
                                                            Constant(value=0.01, kind=None),
                                                            Constant(value=0.9, kind=None),
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
                                            Constant(value='full_name', kind=None),
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
                                                            Constant(value='Industry full name %s', kind=None),
                                                        ],
                                                        ctx=Load(),
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
    ],
    type_ignores=[],
)
