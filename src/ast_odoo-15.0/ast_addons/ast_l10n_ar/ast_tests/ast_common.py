Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='Form', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.account.tests.common',
            names=[alias(name='AccountTestInvoicingCommon', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
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
            name='TestAr',
            bases=[Name(id='AccountTestInvoicingCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='chart_template_ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='l10n_ar.l10nar_ri_chart_template', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestAr', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='chart_template_ref',
                                        value=Name(id='chart_template_ref', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='company_data',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='parent_id', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='l10n_ar_afip_start_date', kind=None),
                                            Constant(value='l10n_ar_gross_income_type', kind=None),
                                            Constant(value='l10n_ar_gross_income_number', kind=None),
                                        ],
                                        values=[
                                            Attribute(
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
                                                    args=[Constant(value='base.main_company', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.ARS', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='(AR) Responsable Inscripto (Unit Tests)', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='%Y-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='local', kind=None),
                                            Constant(value='901-21885123', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_ri',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='company_ri',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                            Constant(value='vat', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='website', kind=None),
                                        ],
                                        values=[
                                            Constant(value='(AR) Responsable Inscripto (Unit Tests)', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_IVARI', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.it_cuit', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='30111111118', kind=None),
                                            Constant(value='Calle Falsa 123', kind=None),
                                            Constant(value='Rosario', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='base.ar', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.state_ar_s', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='2000', kind=None),
                                            Constant(value='+1 555 123 8069', kind=None),
                                            Constant(value='info@example.com', kind=None),
                                            Constant(value='www.example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_ri',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_ri',
                                    ctx=Load(),
                                ),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_mono',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='setup_company_data',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='(AR) Monotributista (Unit Tests)', kind=None)],
                                    keywords=[
                                        keyword(
                                            arg='chart_template',
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
                                                args=[Constant(value='l10n_ar.l10nar_base_chart_template', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                slice=Constant(value='company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='company_mono',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='parent_id', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='l10n_ar_afip_start_date', kind=None),
                                            Constant(value='l10n_ar_gross_income_type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
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
                                                    args=[Constant(value='base.main_company', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.ARS', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='(AR) Monotributista (Unit Tests)', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='%Y-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='exempt', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='company_mono',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                            Constant(value='vat', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='website', kind=None),
                                        ],
                                        values=[
                                            Constant(value='(AR) Monotributista (Unit Tests)', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_RM', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.it_cuit', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='20222222223', kind=None),
                                            Constant(value='Calle Falsa 123', kind=None),
                                            Constant(value='Rosario', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='base.ar', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.state_ar_s', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='2000', kind=None),
                                            Constant(value='+1 555 123 8069', kind=None),
                                            Constant(value='info@example.com', kind=None),
                                            Constant(value='www.example.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_mono',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_mono',
                                    ctx=Load(),
                                ),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='bank_account_ri',
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
                                        slice=Constant(value='res.partner.bank', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='acc_number', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='company_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='7982898111100056688080', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='company_ri',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_ri',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='res_partner_adhoc',
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
                                            Constant(value='is_company', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='website', kind=None),
                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                            Constant(value='vat', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='ADHOC SA', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='Rosario', kind=None),
                                            Constant(value='2000', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='base.state_ar_s', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.ar', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Ovidio Lagos 41 bis', kind=None),
                                            Constant(value='info@adhoc.com.ar', kind=None),
                                            Constant(value='(+54) (341) 208 0203', kind=None),
                                            Constant(value='http://www.adhoc.com.ar', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.it_cuit', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='30714295698', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_IVARI', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_cf',
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
                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Consumidor Final Anónimo', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.it_Sigd', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_CF', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='res_partner_gritti_mono',
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
                                            Constant(value='is_company', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='website', kind=None),
                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                            Constant(value='vat', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Gritti Agrimensura (Monotributo)', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='Rosario', kind=None),
                                            Constant(value='2000', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='base.state_ar_s', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.ar', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Calle Falsa 123', kind=None),
                                            Constant(value='info@example.com.ar', kind=None),
                                            Constant(value='(+54) (341) 111 2222', kind=None),
                                            Constant(value='http://www.grittiagrimensura.com', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.it_cuit', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='27320732811', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_RM', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='res_partner_cerrocastor',
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
                                            Constant(value='is_company', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='website', kind=None),
                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                            Constant(value='vat', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Cerro Castor (Tierra del Fuego)', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='Ushuaia', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='base.state_ar_v', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.ar', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Ruta 3 km 26', kind=None),
                                            Constant(value='info@cerrocastor.com', kind=None),
                                            Constant(value='(+00) (11) 4444 5556', kind=None),
                                            Constant(value='http://www.cerrocastor.com', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.it_cuit', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='27333333339', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_IVA_LIB', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='res_partner_cmr',
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
                                            Constant(value='is_company', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='website', kind=None),
                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                            Constant(value='vat', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Concejo Municipal de Rosario (IVA Sujeto Exento)', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='Rosario', kind=None),
                                            Constant(value='2000', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='base.state_ar_s', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.ar', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Cordoba 501', kind=None),
                                            Constant(value='info@example.com.ar', kind=None),
                                            Constant(value='(+54) (341) 222 3333', kind=None),
                                            Constant(value='http://www.concejorosario.gov.ar/', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.it_cuit', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='30684679372', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_IVAE', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='res_partner_expresso',
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
                                            Constant(value='is_company', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='website', kind=None),
                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                            Constant(value='vat', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Expresso', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='Barcelona', kind=None),
                                            Constant(value='11002', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='base.es', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='La gran avenida 123', kind=None),
                                            Constant(value='info@expresso.com', kind=None),
                                            Constant(value='(+00) (11) 222 3333', kind=None),
                                            Constant(value='http://www.expresso.com/', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_latam_base.it_fid', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='2222333344445555', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_EXT', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_mipyme',
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
                                            Constant(value='is_company', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='website', kind=None),
                                            Constant(value='l10n_latam_identification_type_id', kind=None),
                                            Constant(value='vat', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Belgrano Cargas Y Logistica S (Mipyme)', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='Buenos Aires', kind=None),
                                            Constant(value='1425', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='base.state_ar_c', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
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
                                                    args=[Constant(value='base.ar', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Av. Santa Fe 4636', kind=None),
                                            Constant(value='mipyme@example.com', kind=None),
                                            Constant(value='(123)-456-7890', kind=None),
                                            Constant(value='http://www.mypime-inc.com', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.it_cuit', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='30714101443', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_IVARI', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_mipyme_ex',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='partner_mipyme',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='l10n_ar_afip_responsibility_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='MiPyme Exento', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='l10n_ar.res_IVAE', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_21',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_search_tax',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Constant(value='iva_21', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_27',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_search_tax',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Constant(value='iva_27', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_0',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_search_tax',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Constant(value='iva_0', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_10_5',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_search_tax',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Constant(value='iva_105', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_no_gravado',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_search_tax',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Constant(value='iva_no_gravado', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_perc_iibb',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_search_tax',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Constant(value='percepcion_iibb_ba', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_iva_exento',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_search_tax',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Constant(value='iva_exento', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_unit', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_hour', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_hour', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='product_iva_21',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='lst_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='default_code', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Large Cabinet (VAT 21)', kind=None),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=320.0, kind=None),
                                            Constant(value='consu', kind=None),
                                            Constant(value='E-COM07', kind=None),
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
                                    attr='service_iva_27',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='lst_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Telephone service (VAT 27)', kind=None),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=130.0, kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='TELEFONIA', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='tax_27',
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
                                    attr='product_iva_cero',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Non-industrialized animals and vegetables (VAT Zero)', kind=None),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=160.0, kind=None),
                                            Constant(value='consu', kind=None),
                                            Constant(value='CERO', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='tax_0',
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
                                    attr='product_iva_105',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Laptop Customized (VAT 10,5)', kind=None),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='consu', kind=None),
                                            Constant(value='10,5', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='tax_10_5',
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
                                    attr='service_iva_21',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Virtual Home Staging (VAT 21)', kind=None),
                                            Attribute(
                                                value=Name(id='uom_hour', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_hour', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=38.25, kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='VAT 21', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='tax_21',
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
                                    attr='product_no_gravado',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Untaxed concepts (VAT NT)', kind=None),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=40.0, kind=None),
                                            Constant(value='consu', kind=None),
                                            Constant(value='NOGRAVADO', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='tax_no_gravado',
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
                                    attr='product_iva_105_perc',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='product_iva_105',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Laptop E5023 (VAT 10,5)', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='tax_10_5',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='tax_perc_iibb',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='product_iva_exento',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='taxes_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Book: Development in Odoo (VAT Exempt)', kind=None),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=80.0, kind=None),
                                            Constant(value='consu', kind=None),
                                            Constant(value='EXENTO', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='tax_iva_exento',
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
                                    attr='document_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='invoice_a', kind=None),
                                    Constant(value='credit_note_a', kind=None),
                                    Constant(value='invoice_b', kind=None),
                                    Constant(value='credit_note_b', kind=None),
                                    Constant(value='invoice_e', kind=None),
                                    Constant(value='invoice_mipyme_a', kind=None),
                                    Constant(value='invoice_mipyme_b', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_ar.dc_a_f', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_ar.dc_a_nc', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_ar.dc_b_f', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_ar.dc_b_nc', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_ar.dc_e_f', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_ar.dc_fce_a_f', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_ar.dc_fce_b_f', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='sale_expo_journal_ri',
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
                                        slice=Constant(value='account.journal', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='code', kind=None),
                                            Constant(value='l10n_latam_use_documents', kind=None),
                                            Constant(value='l10n_ar_afip_pos_number', kind=None),
                                            Constant(value='l10n_ar_afip_pos_partner_id', kind=None),
                                            Constant(value='l10n_ar_afip_pos_system', kind=None),
                                            Constant(value='refund_sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Expo Sales Journal', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='company_ri',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='sale', kind=None),
                                            Constant(value='S0002', kind=None),
                                            Constant(value='True', kind=None),
                                            Constant(value=2, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='partner_ri',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='FEERCEL', kind=None),
                                            Constant(value=False, kind=None),
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
                                    attr='demo_invoices',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_test_invoices_like_demo',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='use_current_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create in the unit tests the same invoices created in demo data ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='payment_term_id', ctx=Store())],
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
                                args=[Constant(value='account.account_payment_term_end_following_month', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_user_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='incoterm', ctx=Store())],
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
                                args=[Constant(value='account.incoterm_EXW', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoices_to_create', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='test_invoice_1', kind=None),
                                    Constant(value='test_invoice_2', kind=None),
                                    Constant(value='test_invoice_3', kind=None),
                                    Constant(value='test_invoice_4', kind=None),
                                    Constant(value='test_invoice_5', kind=None),
                                    Constant(value='test_invoice_6', kind=None),
                                    Constant(value='test_invoice_7', kind=None),
                                    Constant(value='test_invoice_8', kind=None),
                                    Constant(value='test_invoice_10', kind=None),
                                    Constant(value='test_invoice_11', kind=None),
                                    Constant(value='test_invoice_12', kind=None),
                                    Constant(value='test_invoice_13', kind=None),
                                    Constant(value='test_invoice_14', kind=None),
                                    Constant(value='test_invoice_15', kind=None),
                                    Constant(value='test_invoice_16', kind=None),
                                    Constant(value='test_invoice_17', kind=None),
                                    Constant(value='test_invoice_18', kind=None),
                                    Constant(value='test_invoice_19', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_1: Invoice to gritti support service, vat 21', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_gritti_mono',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[Constant(value='product_id', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_2: Invoice to CMR with vat 21, 27 and 10,5', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_cmr',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=642.0, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_27',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=250.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105_perc',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=3245.0, kind=None),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_3: Invoice to ADHOC with vat cero and 21', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=642.0, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_cero',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=200.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_4: Invoice to ADHOC with vat exempt and 21', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=642.0, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_exento',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=100.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_5: Invoice to ADHOC with all type of taxes', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=642.0, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_27',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=250.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105_perc',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=3245.0, kind=None),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_no_gravado',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=50.0, kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_cero',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=200.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_exento',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=100.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_incoterm_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_6: Invoice to cerro castor, fiscal position changes taxes to exempt', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_cerrocastor',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sale_expo_journal_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='incoterm', ctx=Load()),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=642.0, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_27',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=250.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105_perc',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=3245.0, kind=None),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_no_gravado',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=50.0, kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_cero',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=200.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_exento',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=100.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_incoterm_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_7: Export invoice to expresso, fiscal position changes tax to exempt (type 4 because it have services)', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_expresso',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sale_expo_journal_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='incoterm', ctx=Load()),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=642.0, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_27',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=250.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105_perc',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=3245.0, kind=None),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_no_gravado',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=50.0, kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_cero',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=200.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_exento',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=100.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_8: Invoice to consumidor final', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner_cf',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=642.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                            Constant(value='currency_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_10; Invoice to ADHOC in USD and vat 21', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=1000.0, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='base.USD', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_11: Invoice to ADHOC with many lines in order to prove rounding error, with 4 decimals of precision for the currency and 2 decimals for the product the error apperar', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=1.12, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Support Services 1', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=1.12, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Support Services 2', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=1.12, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Support Services 3', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=1.12, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Support Services 4', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_12: Invoice to ADHOC with many lines in order to test rounding error, it is required to use a 4 decimal precision in prodct in order to the error occur', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=15.7076, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Support Services 1', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=5.3076, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value='Support Services 2', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=3.5384, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value='Support Services 3', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=1.6376, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value='Support Services 4', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_13: Invoice to ADHOC with many lines in order to test zero amount invoices y rounding error. it is required to set the product decimal precision to 4 and change 260.59 for 260.60 in order to reproduce the error', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=24.3, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value='Support Services 1', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=260.59, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Support Services 2', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=48.72, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Support Services 3', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=13.666, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Support Services 4', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=11.329, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value='Support Services 5', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=68.9408, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Support Services 6', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=4.7881, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value='Support Services 7', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=12.0625, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value='Support Services 8', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_incoterm_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_14: Export invoice to expresso, fiscal position changes tax to exempt (type 1 because only products)', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_expresso',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sale_expo_journal_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='incoterm', ctx=Load()),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=642.0, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_incoterm_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_15: Export invoice to expresso, fiscal position changes tax to exempt (type 2 because only service)', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_expresso',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sale_expo_journal_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='incoterm', ctx=Load()),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_27',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=250.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='journal_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_incoterm_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_16: Export invoice to expresso, fiscal position changes tax to exempt (type 1 because it have products only, used to test refund of expo)', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_expresso',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sale_expo_journal_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            Name(id='incoterm', ctx=Load()),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=642.0, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_17: Invoice to ADHOC with 100%% of discount', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='discount', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=24.3, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value='Support Services 8', kind=None),
                                                            Constant(value=100, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_18: Invoice to ADHOC with 100%% of discount and with different VAT aliquots', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='discount', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=24.3, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value='Support Services 8', kind=None),
                                                            Constant(value=100, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='discount', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_27',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=250.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=100, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105_perc',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=3245.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_user_id', kind=None),
                                            Constant(value='invoice_payment_term_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='company_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_invoice_19: Invoice to ADHOC with multiple taxes and perceptions', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='res_partner_adhoc',
                                                ctx=Load(),
                                            ),
                                            Name(id='invoice_user_id', ctx=Load()),
                                            Name(id='payment_term_id', ctx=Load()),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_ri',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_21',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=24.3, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value='Support Services 8', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='service_iva_27',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=250.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='price_unit', kind=None),
                                                            Constant(value='quantity', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_iva_105_perc',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=3245.0, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='invoices_to_create', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='Form', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='account.move', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='default_move_type',
                                                                value=Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='move_type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='invoice_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='ref',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='ref', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='partner_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='invoice_user_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='invoice_user_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='invoice_payment_term_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='invoice_payment_term_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='use_current_date', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='invoice_date',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='invoice_date', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='invoice_incoterm_id', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='invoice_incoterm_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='invoice_incoterm_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='line', ctx=Store()),
                                            iter=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='invoice_line_ids', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                With(
                                                    items=[
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_form', ctx=Load()),
                                                                        attr='invoice_line_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='new',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            optional_vars=Name(id='line_form', ctx=Store()),
                                                        ),
                                                    ],
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='line_form', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='product_id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='line_form', ctx=Load()),
                                                                    attr='price_unit',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='price_unit', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='line_form', ctx=Load()),
                                                                    attr='quantity',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='quantity', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='line_form', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='xxxx', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='line_form', ctx=Load()),
                                                                    attr='account_id',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='company_data',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='default_account_revenue', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoice_form', ctx=Load()),
                                            attr='save',
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
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='demo_invoices',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='key', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='invoice', ctx=Load()),
                                    type_comment=None,
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
                    name='_get_afip_pos_system_real_name',
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
                        Return(
                            value=Dict(
                                keys=[Constant(value='PREPRINTED', kind=None)],
                                values=[Constant(value='II_IM', kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_journal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='afip_ws', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create a journal of a given AFIP ws type.\n        If there is a problem because we are using a AFIP certificate that is already been in use then change the certificate and try again ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='data', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='afip_ws', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='afip_ws', ctx=Load()),
                                    attr='upper',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pos_number', ctx=Store())],
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='randint',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Constant(value=99999, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='l10n_ar_afip_pos_number', kind=None),
                                ops=[In()],
                                comparators=[Name(id='data', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pos_number', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='l10n_ar_afip_pos_number', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='code', kind=None),
                                    Constant(value='l10n_ar_afip_pos_system', kind=None),
                                    Constant(value='l10n_ar_afip_pos_number', kind=None),
                                    Constant(value='l10n_latam_use_documents', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='l10n_ar_afip_pos_partner_id', kind=None),
                                    Constant(value='sequence', kind=None),
                                ],
                                values=[
                                    BinOp(
                                        left=Constant(value='%s %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='afip_ws', ctx=Load()),
                                                        attr='replace',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='WS', kind=None),
                                                        Constant(value='', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Name(id='pos_number', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='sale', kind=None),
                                    Name(id='afip_ws', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_afip_pos_system_real_name',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='afip_ws', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='pos_number', ctx=Load()),
                                    Constant(value=True, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='partner_ri',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='journal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.journal', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='Created journal %s for company %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='journal', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
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
                        Return(
                            value=Name(id='journal', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='invoice_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='out_invoice', kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='data', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.move', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='default_move_type',
                                                        value=Name(id='invoice_type', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='invoice_form', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='invoice_form', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='partner', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='partner',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='in_', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='invoice_type', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='journal_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='journal', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='journal',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='document_type', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='l10n_latam_document_type_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='document_type', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='document_number', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='l10n_latam_document_number',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='document_number', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='incoterm', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='invoice_incoterm_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='incoterm', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='currency', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='currency', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='lines', kind=None),
                                            List(
                                                elts=[Dict(keys=[], values=[])],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='invoice_form', ctx=Load()),
                                                                attr='invoice_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='new',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='invoice_line_form', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='display_type', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='display_type',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='display_type', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='not invoice line', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='product', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='product_iva_21',
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
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='quantity',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value=1, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                    attr='price_unit',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value=100, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='invoice_form', ctx=Load()),
                                            attr='invoice_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='invoice_form', ctx=Load()),
                                        attr='date',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='invoice', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice_product',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='data', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_invoice',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice_service',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='data', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='newlines', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='lines', kind=None),
                                    List(
                                        elts=[Dict(keys=[], values=[])],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='product', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='service_iva_27',
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
                                            value=Name(id='newlines', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='line', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lines', kind=None)],
                                        values=[Name(id='newlines', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_invoice',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice_product_service',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='data', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='newlines', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='lines', kind=None),
                                    List(
                                        elts=[Dict(keys=[], values=[])],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='product', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_iva_21',
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
                                            value=Name(id='newlines', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='line', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lines', kind=None)],
                                        values=[
                                            BinOp(
                                                left=Name(id='newlines', ctx=Load()),
                                                op=Add(),
                                                right=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[Constant(value='product', kind=None)],
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='service_iva_27',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_invoice',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_credit_note',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='data', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='refund_wizard', ctx=Store())],
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
                                                slice=Constant(value='account.move.reversal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='active_ids', kind=None),
                                                    Constant(value='active_model', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='account.move', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='reason', kind=None),
                                            Constant(value='refund_method', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='reason', kind=None),
                                                    Constant(value='Mercadería defectuosa', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='refund_method', kind=None),
                                                    Constant(value='refund', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='journal_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                            targets=[Name(id='forced_document_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='document_type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='forced_document_type', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='refund_wizard', ctx=Load()),
                                            attr='l10n_latam_document_type_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='forced_document_type', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='refund_wizard', ctx=Load()),
                                    attr='reverse_moves',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='refund', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='res_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='refund', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_debit_note',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='data', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='debit_note_wizard', ctx=Store())],
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
                                                slice=Constant(value='account.debit.note', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='active_ids', kind=None),
                                                    Constant(value='active_model', kind=None),
                                                    Constant(value='default_copy_lines', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='account.move', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='reason', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='reason', kind=None),
                                                    Constant(value='Mercadería defectuosa', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='debit_note_wizard', ctx=Load()),
                                    attr='create_debit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='debit_note', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='res_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='debit_note', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_tax',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tax_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
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
                                                slice=Constant(value='account.tax', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='active_test',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='type_tax_use', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='sale', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='tax_group_id', kind=None),
                                                    Constant(value='=', kind=None),
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
                                                            args=[
                                                                BinOp(
                                                                    left=Constant(value='l10n_ar.tax_group_', kind=None),
                                                                    op=Add(),
                                                                    right=Name(id='tax_type', ctx=Load()),
                                                                ),
                                                            ],
                                                            keywords=[],
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
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='%s Tax was not found', kind=None),
                                        op=Mod(),
                                        right=Name(id='tax_type', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_fp',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='name', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
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
                    name='_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
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
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='posted', kind=None),
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
                    name='_prepare_multicurrency_values',
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
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='groups_id', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
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
                                                                    args=[Constant(value='base.group_multi_currency', kind=None)],
                                                                    keywords=[],
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
                                    attr='_set_today_rate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.ARS', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=1.0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_today_rate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.USD', kind=None)],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Constant(value=1.0, kind=None),
                                        op=Div(),
                                        right=Constant(value=162.013, kind=None),
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
                    name='_set_today_rate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='currency', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='rate_obj', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.currency.rate', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rate', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rate_obj', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='today',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
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
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='rate', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='rate', ctx=Load()),
                                            attr='rate',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='value', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rate_obj', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='rate', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='value', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='external_l10n', kind=None),
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='-standard', kind=None),
                        Constant(value='external', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
