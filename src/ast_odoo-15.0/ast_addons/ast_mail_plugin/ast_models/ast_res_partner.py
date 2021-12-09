Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ResPartner',
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
                    targets=[Name(id='iap_enrich_info', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='IAP Enrich Info', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='IAP response stored as a JSON string', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_partner_iap_info', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='iap_search_domain', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Search Domain / Email', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_partner_iap_info', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_partner_iap_info',
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
                            targets=[Name(id='partner_iaps', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner.iap', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
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
                            targets=[Name(id='partner_iaps_per_partner', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='partner_iap', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Load(),
                                ),
                                value=Name(id='partner_iap', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='partner_iap', ctx=Store()),
                                        iter=Name(id='partner_iaps', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_iap', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partner_iaps_per_partner', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='partner_iap', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='iap_enrich_info',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='partner_iap', ctx=Load()),
                                                attr='iap_enrich_info',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='iap_search_domain',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='partner_iap', ctx=Load()),
                                                attr='iap_search_domain',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='iap_enrich_info',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='iap_search_domain',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
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
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResPartner', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='iap_enrich_info', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='iap_search_domain', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.partner.iap', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='iap_enrich_info', kind=None),
                                                    Constant(value='iap_search_domain', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='vals', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='iap_enrich_info', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='vals', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='iap_search_domain', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='partner', ctx=Load()),
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResPartner', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='iap_enrich_info', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='iap_search_domain', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner_iaps', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.partner.iap', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='partner_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
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
                                    targets=[Name(id='missing_partners', ctx=Store())],
                                    value=Name(id='self', ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='partner_iap', ctx=Store()),
                                    iter=Name(id='partner_iaps', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='iap_enrich_info', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='partner_iap', ctx=Load()),
                                                            attr='iap_enrich_info',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='iap_enrich_info', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Constant(value='iap_search_domain', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='partner_iap', ctx=Load()),
                                                            attr='iap_search_domain',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='iap_search_domain', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='missing_partners', ctx=Store()),
                                            op=Sub(),
                                            value=Attribute(
                                                value=Name(id='partner_iap', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='missing_partners', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.partner.iap', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    ListComp(
                                                        elt=Dict(
                                                            keys=[
                                                                Constant(value='partner_id', kind=None),
                                                                Constant(value='iap_enrich_info', kind=None),
                                                                Constant(value='iap_search_domain', kind=None),
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='vals', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='iap_enrich_info', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='vals', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='iap_search_domain', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='partner', ctx=Store()),
                                                                iter=Name(id='missing_partners', ctx=Load()),
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
                                ),
                            ],
                            orelse=[],
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
