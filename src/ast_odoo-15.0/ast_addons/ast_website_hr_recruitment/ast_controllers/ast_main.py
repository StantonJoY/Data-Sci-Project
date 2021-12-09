Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='slug', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='NotFound', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteHrRecruitment',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='sitemap_jobs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                            arg(arg='qs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='qs', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='qs', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[Constant(value='/jobs', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Dict(
                                            keys=[Constant(value='loc', kind=None)],
                                            values=[Constant(value='/jobs', kind=None)],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='jobs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='country', annotation=None, type_comment=None),
                            arg(arg='department', annotation=None, type_comment=None),
                            arg(arg='office_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='show_address',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                                keyword(
                                                    arg='no_tag_br',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Country', ctx=Store())],
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='res.country', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Jobs', ctx=Store())],
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='hr.job', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='website_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='job_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Jobs', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='domain', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='order',
                                            value=Constant(value='is_published desc, sequence, no_of_recruitment desc', kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='jobs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Jobs', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='job_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=Or(),
                                    values=[
                                        Name(id='country', ctx=Load()),
                                        Name(id='department', ctx=Load()),
                                        Name(id='office_id', ctx=Load()),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='kwargs', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='all_countries', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='country_code', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='geoip', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='country_code', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='country_code', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='countries_', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Country', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='code', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='country_code', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='country', ctx=Store())],
                                            value=IfExp(
                                                test=Name(id='countries_', ctx=Load()),
                                                body=Subscript(
                                                    value=Name(id='countries_', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=None, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='any', ctx=Load()),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=Name(id='j', ctx=Load()),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='j', ctx=Store()),
                                                                    iter=Name(id='jobs', ctx=Load()),
                                                                    ifs=[
                                                                        BoolOp(
                                                                            op=And(),
                                                                            values=[
                                                                                Attribute(
                                                                                    value=Name(id='j', ctx=Load()),
                                                                                    attr='address_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Compare(
                                                                                    left=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='j', ctx=Load()),
                                                                                            attr='address_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='country_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Name(id='country', ctx=Load())],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='country', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='country', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='kwargs', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='all_countries', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='jobs', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='j', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='j', ctx=Store()),
                                                iter=Name(id='jobs', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='j', ctx=Load()),
                                                                    attr='address_id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Is()],
                                                                comparators=[Constant(value=None, kind=None)],
                                                            ),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='j', ctx=Load()),
                                                                            attr='address_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='country_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='j', ctx=Load()),
                                                                                    attr='address_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='country_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='country', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='offices', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='j', ctx=Load()),
                                                    attr='address_id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='j', ctx=Store()),
                                                        iter=Name(id='jobs', ctx=Load()),
                                                        ifs=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='j', ctx=Load()),
                                                                            attr='address_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Is()],
                                                                        comparators=[Constant(value=None, kind=None)],
                                                                    ),
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='j', ctx=Load()),
                                                                                    attr='address_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='country_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='j', ctx=Load()),
                                                                                            attr='address_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='country_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='country', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='offices', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='j', ctx=Load()),
                                                    attr='address_id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='j', ctx=Store()),
                                                        iter=Name(id='jobs', ctx=Load()),
                                                        ifs=[
                                                            Attribute(
                                                                value=Name(id='j', ctx=Load()),
                                                                attr='address_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='departments', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='j', ctx=Load()),
                                            attr='department_id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='j', ctx=Store()),
                                                iter=Name(id='jobs', ctx=Load()),
                                                ifs=[
                                                    Attribute(
                                                        value=Name(id='j', ctx=Load()),
                                                        attr='department_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='countries', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='o', ctx=Load()),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='o', ctx=Store()),
                                                iter=Name(id='offices', ctx=Load()),
                                                ifs=[
                                                    Attribute(
                                                        value=Name(id='o', ctx=Load()),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='department', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='jobs', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='j', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='j', ctx=Store()),
                                                iter=Name(id='jobs', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='j', ctx=Load()),
                                                                attr='department_id',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='j', ctx=Load()),
                                                                        attr='department_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='department', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='office_id', ctx=Load()),
                                    Compare(
                                        left=Name(id='office_id', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Name(id='x', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Name(id='offices', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='jobs', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='j', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='j', ctx=Store()),
                                                iter=Name(id='jobs', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='j', ctx=Load()),
                                                                attr='address_id',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='j', ctx=Load()),
                                                                        attr='address_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='office_id', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='office_id', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_hr_recruitment.index', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='jobs', kind=None),
                                            Constant(value='countries', kind=None),
                                            Constant(value='departments', kind=None),
                                            Constant(value='offices', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='department_id', kind=None),
                                            Constant(value='office_id', kind=None),
                                        ],
                                        values=[
                                            Name(id='jobs', ctx=Load()),
                                            Name(id='countries', ctx=Load()),
                                            Name(id='departments', ctx=Load()),
                                            Name(id='offices', ctx=Load()),
                                            Name(id='country', ctx=Load()),
                                            Name(id='department', ctx=Load()),
                                            Name(id='office_id', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/jobs', kind=None),
                                        Constant(value='/jobs/country/<model("res.country"):country>', kind=None),
                                        Constant(value='/jobs/department/<model("hr.department"):department>', kind=None),
                                        Constant(value='/jobs/country/<model("res.country"):country>/department/<model("hr.department"):department>', kind=None),
                                        Constant(value='/jobs/office/<int:office_id>', kind=None),
                                        Constant(value='/jobs/country/<model("res.country"):country>/office/<int:office_id>', kind=None),
                                        Constant(value='/jobs/department/<model("hr.department"):department>/office/<int:office_id>', kind=None),
                                        Constant(value='/jobs/country/<model("res.country"):country>/department/<model("hr.department"):department>/office/<int:office_id>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Name(id='sitemap_jobs', ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='jobs_add',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='job', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='hr.job', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='rendering_bundle',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Job Title', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='/jobs/detail/%s?enable_editor=1', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='slug', ctx=Load()),
                                            args=[Name(id='job', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/jobs/add', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='jobs_detail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='job', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_hr_recruitment.detail', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='job', kind=None),
                                            Constant(value='main_object', kind=None),
                                        ],
                                        values=[
                                            Name(id='job', ctx=Load()),
                                            Name(id='job', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/jobs/detail/<model("hr.job"):job>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='jobs_apply',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='job', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='error', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='website_hr_recruitment_error', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='error', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website_hr_recruitment_error', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='default', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website_hr_recruitment_default', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_hr_recruitment.apply', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='job', kind=None),
                                            Constant(value='error', kind=None),
                                            Constant(value='default', kind=None),
                                        ],
                                        values=[
                                            Name(id='job', ctx=Load()),
                                            Name(id='error', ctx=Load()),
                                            Name(id='default', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/jobs/apply/<model("hr.job"):job>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
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
