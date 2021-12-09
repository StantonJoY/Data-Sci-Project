Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='pytz',
            names=[alias(name='timezone', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='misc', asname=None),
                alias(name='float_compare', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.account_edi.tests.common',
            names=[alias(name='AccountEdiTestCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestEsEdiCommon',
            bases=[Name(id='AccountEdiTestCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='chart_template_ref', annotation=None, type_comment=None),
                            arg(arg='edi_format_ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='l10n_es.account_chart_template_full', kind=None),
                            Constant(value='l10n_es_edi_sii.edi_es_sii', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
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
                                    keyword(
                                        arg='edi_format_ref',
                                        value=Name(id='edi_format_ref', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='frozen_today',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='year',
                                        value=Constant(value=2019, kind=None),
                                    ),
                                    keyword(
                                        arg='month',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='day',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='hour',
                                        value=Constant(value=0, kind=None),
                                    ),
                                    keyword(
                                        arg='minute',
                                        value=Constant(value=0, kind=None),
                                    ),
                                    keyword(
                                        arg='second',
                                        value=Constant(value=0, kind=None),
                                    ),
                                    keyword(
                                        arg='tzinfo',
                                        value=Call(
                                            func=Name(id='timezone', ctx=Load()),
                                            args=[Constant(value='utc', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='maxDiff',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='certificate',
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
                                        slice=Constant(value='l10n_es_edi.certificate', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='content', kind=None),
                                            Constant(value='password', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='encodebytes',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='misc', ctx=Load()),
                                                                    attr='file_open',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='l10n_es_edi_sii/demo/certificates/sello_entidad_act.p12', kind=None),
                                                                    Constant(value='rb', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='IZDesa2021', kind=None),
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
                                            Constant(value='country_id', kind=None),
                                            Constant(value='state_id', kind=None),
                                            Constant(value='l10n_es_edi_certificate_id', kind=None),
                                            Constant(value='vat', kind=None),
                                            Constant(value='l10n_es_edi_test_env', kind=None),
                                            Constant(value='l10n_es_edi_tax_agency', kind=None),
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
                                                    args=[Constant(value='base.es', kind=None)],
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
                                                    args=[Constant(value='base.state_es_z', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='certificate',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ES59962470K', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='bizkaia', kind=None),
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
                                        value=Name(id='cls', ctx=Load()),
                                        attr='partner_a',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='vat', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='BE0477472701', kind=None),
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
                                                    args=[Constant(value='base.be', kind=None)],
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='partner_b',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='vat', kind=None)],
                                        values=[Constant(value='ESF35999705', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='product_t',
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test product', kind=None)],
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
                                    attr='partner_t',
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
                                            Constant(value='vat', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test partner', kind=None),
                                            Constant(value='ESF35999705', kind=None),
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
                    name='_get_tax_by_xml_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='trailing_xml_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Helper to retrieve a tax easily.\n\n        :param trailing_xml_id: The trailing tax's xml id.\n        :return:                An account.tax record\n        ", kind=None),
                        ),
                        Return(
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
                                args=[
                                    JoinedStr(
                                        values=[
                                            Constant(value='l10n_es.', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='_account_tax_template_', kind=None),
                                            FormattedValue(
                                                value=Name(id='trailing_xml_id', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
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
                    name='create_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
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
                                                arg='edi_test_mode',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_date', kind=None),
                                            Constant(value='date', kind=None),
                                            None,
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='2019-01-01', kind=None),
                                            Constant(value='2019-01-01', kind=None),
                                            Name(id='kwargs', ctx=Load()),
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='product_id', kind=None),
                                                                Constant(value='price_unit', kind=None),
                                                                None,
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='product_a',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value=1000.0, kind=None),
                                                                Name(id='line_vals', ctx=Load()),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='line_vals', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='kwargs', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='invoice_line_ids', kind=None),
                                                                List(elts=[], ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install_l10n', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
