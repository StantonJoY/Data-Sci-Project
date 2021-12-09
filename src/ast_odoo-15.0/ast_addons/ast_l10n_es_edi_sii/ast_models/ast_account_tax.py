Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='SIIAccountTaxMixin',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='l10n_es.sii.account.tax.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='SII Fields', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_es_exempt_reason', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='E1', kind=None),
                                                Constant(value='Art. 20', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='E2', kind=None),
                                                Constant(value='Art. 21', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='E3', kind=None),
                                                Constant(value='Art. 22', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='E4', kind=None),
                                                Constant(value='Art. 23 y 24', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='E5', kind=None),
                                                Constant(value='Art. 25', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='E6', kind=None),
                                                Constant(value='Otros', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Exempt Reason (Spain)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_es_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='exento', kind=None),
                                                Constant(value='Exento', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='sujeto', kind=None),
                                                Constant(value='Sujeto', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='sujeto_agricultura', kind=None),
                                                Constant(value='Sujeto Agricultura', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='sujeto_isp', kind=None),
                                                Constant(value='Sujeto ISP', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='no_sujeto', kind=None),
                                                Constant(value='No Sujeto', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='no_sujeto_loc', kind=None),
                                                Constant(value='No Sujeto por reglas de Localization', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='no_deducible', kind=None),
                                                Constant(value='No Deducible', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='retencion', kind=None),
                                                Constant(value='Retencion', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='recargo', kind=None),
                                                Constant(value='Recargo de Equivalencia', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='ignore', kind=None),
                                                Constant(value='Ignore even the base amount', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Tax Type (Spain)', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='sujeto', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_es_bien_inversion', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Bien de Inversion', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AccountTax',
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
                    value=List(
                        elts=[
                            Constant(value='account.tax', kind=None),
                            Constant(value='l10n_es.sii.account.tax.mixin', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account.tax', kind=None),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AccountTaxTemplate',
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
                    value=List(
                        elts=[
                            Constant(value='account.tax.template', kind=None),
                            Constant(value='l10n_es.sii.account.tax.mixin', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account.tax.template', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_tax_vals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='tax_template_to_tax', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_tax_vals',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='company', ctx=Load()),
                                    Name(id='tax_template_to_tax', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='vals', ctx=Load()),
                                    slice=Constant(value='l10n_es_exempt_reason', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='l10n_es_exempt_reason',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='vals', ctx=Load()),
                                    slice=Constant(value='l10n_es_type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='l10n_es_type',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='vals', ctx=Load()),
                                    slice=Constant(value='l10n_es_bien_inversion', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='l10n_es_bien_inversion',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='vals', ctx=Load()),
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
