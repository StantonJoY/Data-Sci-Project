Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestFiscalPosition',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Tests for fiscal positions in auto apply (account.fiscal.position).\n    If a partner has a vat number, the fiscal positions with "vat_required=True"\n    are preferred.\n    ', kind=None),
                ),
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
                                            Name(id='TestFiscalPosition', ctx=Load()),
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
                                    attr='fp',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.fiscal.position', kind=None),
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
                                                attr='fp',
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='auto_apply', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='res_partner',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='be',
                                    ctx=Store(),
                                ),
                                Name(id='be', ctx=Store()),
                            ],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='fr',
                                    ctx=Store(),
                                ),
                                Name(id='fr', ctx=Store()),
                            ],
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
                                args=[Constant(value='base.fr', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='mx',
                                    ctx=Store(),
                                ),
                                Name(id='mx', ctx=Store()),
                            ],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='eu',
                                    ctx=Store(),
                                ),
                                Name(id='eu', ctx=Store()),
                            ],
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
                                args=[Constant(value='base.europe', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='state_fr',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.country.state', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='State', kind=None),
                                            ),
                                            keyword(
                                                arg='code',
                                                value=Constant(value='ST', kind=None),
                                            ),
                                            keyword(
                                                arg='country_id',
                                                value=Attribute(
                                                    value=Name(id='fr', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='jc',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='res_partner',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='JCVD', kind=None),
                                            ),
                                            keyword(
                                                arg='vat',
                                                value=Constant(value='BE0477472701', kind=None),
                                            ),
                                            keyword(
                                                arg='country_id',
                                                value=Attribute(
                                                    value=Name(id='be', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='ben',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='res_partner',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='BP', kind=None),
                                            ),
                                            keyword(
                                                arg='country_id',
                                                value=Attribute(
                                                    value=Name(id='be', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='george',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='res_partner',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='George', kind=None),
                                            ),
                                            keyword(
                                                arg='vat',
                                                value=Constant(value='BE0477472701', kind=None),
                                            ),
                                            keyword(
                                                arg='country_id',
                                                value=Attribute(
                                                    value=Name(id='fr', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='alberto',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='res_partner',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='Alberto', kind=None),
                                            ),
                                            keyword(
                                                arg='vat',
                                                value=Constant(value='BE0477472701', kind=None),
                                            ),
                                            keyword(
                                                arg='country_id',
                                                value=Attribute(
                                                    value=Name(id='mx', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='be_nat',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='fp',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='BE-NAT', kind=None),
                                            ),
                                            keyword(
                                                arg='auto_apply',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='country_id',
                                                value=Attribute(
                                                    value=Name(id='be', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='vat_required',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=10, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='fr_b2c',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='fp',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='EU-VAT-FR-B2C', kind=None),
                                            ),
                                            keyword(
                                                arg='auto_apply',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='country_id',
                                                value=Attribute(
                                                    value=Name(id='fr', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='vat_required',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=40, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='fr_b2b',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='fp',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='EU-VAT-FR-B2B', kind=None),
                                            ),
                                            keyword(
                                                arg='auto_apply',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='country_id',
                                                value=Attribute(
                                                    value=Name(id='fr', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='vat_required',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=50, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_10_fp_country',
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
                        FunctionDef(
                            name='assert_fp',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='partner', annotation=None, type_comment=None),
                                    arg(arg='expected_pos', annotation=None, type_comment=None),
                                    arg(arg='message', annotation=None, type_comment=None),
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='fp',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get_fiscal_position',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='expected_pos', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='message', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='george', ctx=Store()),
                                        Name(id='jc', ctx=Store()),
                                        Name(id='ben', ctx=Store()),
                                        Name(id='alberto', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='george',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jc',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ben',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='alberto',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGreater',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='fr_b2b',
                                            ctx=Load(),
                                        ),
                                        attr='sequence',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='fr_b2c',
                                            ctx=Load(),
                                        ),
                                        attr='sequence',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='george', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FR-B2B should have precedence over FR-B2C', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b',
                                        ctx=Load(),
                                    ),
                                    attr='auto_apply',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='george', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2c',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FR-B2C should match now', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b',
                                        ctx=Load(),
                                    ),
                                    attr='auto_apply',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='eu_intra_b2b',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fp',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='EU-INTRA B2B', kind=None),
                                            ),
                                            keyword(
                                                arg='auto_apply',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='country_group_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='eu',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='vat_required',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=20, kind=None),
                                            ),
                                        ],
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
                                    attr='world',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fp',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=Constant(value='WORLD-EXTRA', kind=None),
                                            ),
                                            keyword(
                                                arg='auto_apply',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='vat_required',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=30, kind=None),
                                            ),
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
                                    attr='assertGreater',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='fr_b2b',
                                            ctx=Load(),
                                        ),
                                        attr='sequence',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eu_intra_b2b',
                                            ctx=Load(),
                                        ),
                                        attr='sequence',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='george', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FR-B2B should have precedence over EU-INTRA B2B', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGreater',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='eu_intra_b2b',
                                            ctx=Load(),
                                        ),
                                        attr='sequence',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='be_nat',
                                            ctx=Load(),
                                        ),
                                        attr='sequence',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='jc', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='eu_intra_b2b',
                                        ctx=Load(),
                                    ),
                                    Constant(value='EU-INTRA B2B should match before BE-NAT', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='ben', ctx=Load()),
                                        attr='vat',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='ben', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='be_nat',
                                        ctx=Load(),
                                    ),
                                    Constant(value='BE-NAT should match before EU-INTRA due to lower sequence', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='be',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='country_group_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=3, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='eu',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='jc', ctx=Load()),
                                        attr='vat',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='jc', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='be_nat',
                                        ctx=Load(),
                                    ),
                                    Constant(value='BE-NAT should match as fallback even w/o VAT match', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='alberto', ctx=Load()),
                                        attr='vat',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='alberto', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='world',
                                        ctx=Load(),
                                    ),
                                    Constant(value='WORLD-EXTRA should match anything else (1)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='alberto', ctx=Load()),
                                    attr='vat',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='alberto', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='world',
                                        ctx=Load(),
                                    ),
                                    Constant(value='WORLD-EXTRA should match anything else (2)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='fr_b2b_zip100',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='zip_from',
                                                value=Constant(value=0, kind=None),
                                            ),
                                            keyword(
                                                arg='zip_to',
                                                value=Constant(value=5000, kind=None),
                                            ),
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=60, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='george', ctx=Load()),
                                    attr='zip',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=6000, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='george', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FR-B2B with wrong zip range should not match', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='george', ctx=Load()),
                                    attr='zip',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=3000, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='george', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b_zip100',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FR-B2B with zip range should have precedence', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='fr_b2b_state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='state_ids',
                                                value=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=4, kind=None),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='state_fr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='sequence',
                                                value=Constant(value=70, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='george', ctx=Load()),
                                    attr='state_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='state_fr',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='george', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b_zip100',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FR-B2B with zip should have precedence over states', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='george', ctx=Load()),
                                    attr='zip',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='george', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fr_b2b_state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FR-B2B with states should have precedence', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='george', ctx=Load()),
                                    attr='property_account_position_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='be_nat',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='assert_fp', ctx=Load()),
                                args=[
                                    Name(id='george', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='be_nat',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Forced position has max precedence', kind=None),
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
                    name='test_20_fp_one_tax_2m',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='src_tax',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='SRC', kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
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
                                    attr='dst1_tax',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='DST1', kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
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
                                    attr='dst2_tax',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount', kind=None),
                                        ],
                                        values=[
                                            Constant(value='DST2', kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
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
                                    attr='fp2m',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fp',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='tax_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='FP-TAX2TAXES', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_src_id', kind=None),
                                                                    Constant(value='tax_dest_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='src_tax',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='dst1_tax',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='tax_src_id', kind=None),
                                                                    Constant(value='tax_dest_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='src_tax',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='dst2_tax',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapped_taxes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fp2m',
                                        ctx=Load(),
                                    ),
                                    attr='map_tax',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='src_tax',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mapped_taxes', ctx=Load()),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dst1_tax',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dst2_tax',
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
