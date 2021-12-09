Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Lead',
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
                    value=Constant(value='crm.lead', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='visitor_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='website.visitor', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Web Visitors', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='visitor_page_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='# Page Views', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_visitor_page_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_visitor_page_count',
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
                            targets=[Name(id='mapped_data', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='visitor_ids', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='sql', ctx=Store())],
                                    value=Constant(value=' SELECT l.id as lead_id, count(*) as page_view_count\n                        FROM crm_lead l\n                        JOIN crm_lead_website_visitor_rel lv ON l.id = lv.crm_lead_id\n                        JOIN website_visitor v ON v.id = lv.website_visitor_id\n                        JOIN website_track p ON p.visitor_id = v.id\n                        WHERE l.id in %s\n                        GROUP BY l.id', kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='sql', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='page_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='dictfetchall',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mapped_data', ctx=Store())],
                                    value=DictComp(
                                        key=Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='lead_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        value=Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='page_view_count', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='data', ctx=Store()),
                                                iter=Name(id='page_data', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='lead', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='lead', ctx=Load()),
                                            attr='visitor_page_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mapped_data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='visitor_ids.page_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_redirect_to_page_views',
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
                            targets=[Name(id='visitors', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='visitor_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.website_visitor_page_action', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='domain', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='visitor_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='visitors', ctx=Load()),
                                                attr='ids',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='visitors', ctx=Load()),
                                                    attr='website_track_ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=15, kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='visitors', ctx=Load()),
                                                        attr='website_track_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='page_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='context', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[Constant(value='search_default_group_by_page', kind=None)],
                                        values=[Constant(value='1', kind=None)],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_merge_get_fields_specific',
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
                            targets=[Name(id='fields_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Lead', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_merge_get_fields_specific',
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
                                    value=Name(id='fields_info', ctx=Load()),
                                    slice=Constant(value='visitor_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[
                                        arg(arg='fname', annotation=None, type_comment=None),
                                        arg(arg='leads', annotation=None, type_comment=None),
                                    ],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value=6, kind=None),
                                                Constant(value=0, kind=None),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='leads', ctx=Load()),
                                                        attr='visitor_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='fields_info', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='website_form_input_filter',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='request', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
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
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='medium_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='medium_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='default_get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Constant(value='medium_id', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='medium_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='ref',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='utm.utm_medium_website', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='team_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='team_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='website',
                                                ctx=Load(),
                                            ),
                                            attr='crm_default_team_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='user_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='website',
                                                ctx=Load(),
                                            ),
                                            attr='crm_default_user_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='with_user',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.users', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='has_group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='crm.group_use_lead', kind=None)],
                                    keywords=[],
                                ),
                                body=Constant(value='lead', kind=None),
                                orelse=Constant(value='opportunity', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
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
