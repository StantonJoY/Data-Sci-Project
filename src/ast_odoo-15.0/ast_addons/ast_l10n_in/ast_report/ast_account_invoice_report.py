Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='L10nInAccountInvoiceReport',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='l10n_in.account.invoice.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Account Invoice Statistics', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='date desc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='account_move_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.move', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Account Move', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Accounting Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Invoice Number', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Customer', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_reverse_charge', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reverse Charge', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_in_gst_treatment', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='regular', kind=None),
                                            Constant(value='Registered Business - Regular', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='composition', kind=None),
                                            Constant(value='Registered Business - Composition', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='unregistered', kind=None),
                                            Constant(value='Unregistered Business', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='consumer', kind=None),
                                            Constant(value='Consumer', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='overseas', kind=None),
                                            Constant(value='Overseas', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='special_economic_zone', kind=None),
                                            Constant(value='Special Economic Zone', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='deemed_export', kind=None),
                                            Constant(value='Deemed Export', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='GST Treatment', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='journal_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.journal', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Journal', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='draft', kind=None),
                                            Constant(value='Unposted', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='posted', kind=None),
                                            Constant(value='Posted', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Status', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='igst_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='IGST Amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cgst_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='CGST Amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sgst_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='SGST Amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cess_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Cess Amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price_total', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Total Without Tax', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='total', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Invoice Total', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reversed_entry_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.move', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Refund Invoice', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='From where this Refund is created', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='shipping_bill_number', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Shipping Bill Number', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='shipping_bill_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Shipping Bill Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='shipping_port_code_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='l10n_in.port.code', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Shipping port code', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ecommerce_partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='E-commerce', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='move_type', ctx=Store())],
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
                                                Constant(value='entry', kind=None),
                                                Constant(value='Journal Entry', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='out_invoice', kind=None),
                                                Constant(value='Customer Invoice', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='out_refund', kind=None),
                                                Constant(value='Customer Credit Note', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='in_invoice', kind=None),
                                                Constant(value='Vendor Bill', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='in_refund', kind=None),
                                                Constant(value='Vendor Credit Note', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='out_receipt', kind=None),
                                                Constant(value='Sales Receipt', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='in_receipt', kind=None),
                                                Constant(value='Purchase Receipt', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_vat', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Customer GSTIN', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ecommerce_vat', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='E-commerce GSTIN', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tax_rate', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Rate', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='place_of_supply', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Place of Supply', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_pre_gst', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Is Pre GST', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_ecommerce', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Is E-commerce', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='b2cl_is_ecommerce', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='B2CL Is E-commerce', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='b2cs_is_ecommerce', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='B2CS Is E-commerce', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='supply_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Supply Type', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='export_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Export Type', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='refund_export_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='UR Type', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='b2b_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='B2B Invoice Type', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='refund_invoice_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Document Type', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='gst_format_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Formated Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='gst_format_refund_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Formated Refund Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='gst_format_shipping_bill_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Formated Shipping Bill Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tax_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.tax', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Tax', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_select',
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
                            targets=[Name(id='select_str', ctx=Store())],
                            value=Constant(value="\n            SELECT min(sub.id) as id,\n            sub.move_id,\n            sub.account_move_id,\n            sub.name,\n            sub.state,\n            sub.partner_id,\n            sub.date,\n            sub.l10n_in_gst_treatment,\n            sub.ecommerce_partner_id,\n            sub.shipping_bill_number,\n            sub.shipping_bill_date,\n            sub.shipping_port_code_id,\n            sub.total * sub.b2cs_refund_sign as total,\n            sub.journal_id,\n            sub.company_id,\n            sub.move_type,\n            sub.reversed_entry_id,\n            sub.partner_vat,\n            sub.ecommerce_vat,\n            sub.tax_rate as tax_rate,\n            (CASE WHEN count(sub.is_reverse_charge) > 0\n                THEN 'Y'\n                ELSE 'N'\n                END) AS is_reverse_charge,\n            sub.place_of_supply,\n            sub.is_pre_gst,\n            sub.is_ecommerce,\n            sub.b2cl_is_ecommerce,\n            sub.b2cs_is_ecommerce,\n            sub.supply_type,\n            sub.export_type,\n            sub.refund_export_type,\n            sub.b2b_type,\n            sub.refund_invoice_type,\n            sub.gst_format_date,\n            sub.gst_format_refund_date,\n            sub.gst_format_shipping_bill_date,\n            sum(sub.igst_amount) * sub.amount_sign * sub.b2cs_refund_sign AS igst_amount,\n            sum(sub.cgst_amount) * sub.amount_sign * sub.b2cs_refund_sign AS cgst_amount,\n            sum(sub.sgst_amount) * sub.amount_sign * sub.b2cs_refund_sign AS sgst_amount,\n            avg(sub.cess_amount) * sub.amount_sign * sub.b2cs_refund_sign AS cess_amount,\n            sum(sub.price_total) * sub.amount_sign * sub.b2cs_refund_sign AS price_total,\n            sub.tax_id\n        ", kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='select_str', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sub_select',
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
                            targets=[Name(id='sub_select_str', ctx=Store())],
                            value=Constant(value="\n            SELECT aml.id AS id,\n                aml.move_id,\n                aml.partner_id,\n                am.id AS account_move_id,\n                am.name,\n                am.state,\n                am.date,\n                am.l10n_in_gst_treatment AS l10n_in_gst_treatment,\n                am.l10n_in_reseller_partner_id AS ecommerce_partner_id,\n                am.l10n_in_shipping_bill_number AS shipping_bill_number,\n                am.l10n_in_shipping_bill_date AS shipping_bill_date,\n                am.l10n_in_shipping_port_code_id AS shipping_port_code_id,\n                ABS(am.amount_total_signed) AS total,\n                am.journal_id,\n                aj.company_id,\n                am.move_type AS move_type,\n                am.reversed_entry_id AS reversed_entry_id,\n                am.l10n_in_gstin AS partner_vat,\n                CASE WHEN rp.vat IS NULL THEN '' ELSE rp.vat END AS ecommerce_vat,\n                (CASE WHEN at.l10n_in_reverse_charge = True\n                    THEN True\n                    ELSE NULL\n                    END)  AS is_reverse_charge,\n                (CASE WHEN ps.l10n_in_tin IS NOT NULL\n                    THEN concat(ps.l10n_in_tin,'-',ps.name)\n                    WHEN ps.id IS NULL and cps.l10n_in_tin IS NOT NULL\n                    THEN concat(cps.l10n_in_tin,'-',cps.name)\n                    ELSE ''\n                    END) AS place_of_supply,\n                (CASE WHEN am.move_type in ('out_refund', 'in_refund') and refund_am.date <= to_date('2017-07-01', 'YYYY-MM-DD')\n                    THEN 'Y'\n                    ELSE 'N'\n                    END) as is_pre_gst,\n\n                (CASE WHEN am.l10n_in_reseller_partner_id IS NOT NULL\n                    THEN 'Y'\n                    ELSE 'N'\n                    END) as is_ecommerce,\n                (CASE WHEN am.l10n_in_reseller_partner_id IS NOT NULL\n                    THEN 'Y'\n                    ELSE 'N'\n                    END) as b2cl_is_ecommerce,\n                (CASE WHEN am.l10n_in_reseller_partner_id IS NOT NULL\n                    THEN 'E'\n                    ELSE 'OE'\n                    END) as b2cs_is_ecommerce,\n                (CASE WHEN am.l10n_in_state_id = cp.state_id or p.id IS NULL\n                    THEN 'Intra State'\n                    WHEN am.l10n_in_state_id != cp.state_id and p.id IS NOT NULL\n                    THEN 'Inter State'\n                    END) AS supply_type,\n                (CASE WHEN am.l10n_in_gst_treatment in ('deemed_export', 'overseas') and am.amount_tax > 0.00\n                    THEN 'EXPWP'\n                    WHEN am.l10n_in_gst_treatment in ('deemed_export', 'overseas') and am.amount_tax <= 0.00\n                    THEN 'EXPWOP'\n                    ELSE ''\n                    END) AS export_type,\n                (CASE WHEN am.l10n_in_gst_treatment in ('deemed_export', 'overseas') and am.amount_tax > 0.00\n                    THEN 'EXPWP'\n                    WHEN am.l10n_in_gst_treatment in ('deemed_export', 'overseas') and am.amount_tax <= 0.00\n                    THEN 'EXPWOP'\n                    ELSE 'B2CL'\n                    END) AS refund_export_type,\n                (CASE WHEN am.l10n_in_gst_treatment = 'regular'\n                    THEN 'Regular'\n                    WHEN am.l10n_in_gst_treatment = 'deemed_export'\n                    THEN 'Deemed'\n                    WHEN am.l10n_in_gst_treatment = 'overseas' and am.amount_tax > 0.00\n                    THEN 'Export with IGST'\n                    WHEN am.l10n_in_gst_treatment = 'special_economic_zone' and am.amount_tax > 0.00\n                    THEN 'SEZ with IGST payment'\n                    WHEN am.l10n_in_gst_treatment = 'special_economic_zone' and am.amount_tax <= 0.00\n                    THEN 'SEZ without IGST payment'\n                    END) AS b2b_type,\n                (CASE WHEN am.move_type = 'out_refund'\n                    THEN 'C'\n                    WHEN am.move_type = 'in_refund'\n                    THEN 'D'\n                    ELSE ''\n                    END) as refund_invoice_type,\n                (CASE WHEN am.date IS NOT NULL\n                    THEN TO_CHAR(am.date, 'DD-MON-YYYY')\n                    ELSE ''\n                    END) as gst_format_date,\n                (CASE WHEN refund_am.date IS NOT NULL\n                    THEN TO_CHAR(refund_am.date, 'DD-MON-YYYY')\n                    ELSE ''\n                    END) as gst_format_refund_date,\n                (CASE WHEN am.l10n_in_shipping_bill_date IS NOT NULL\n                    THEN TO_CHAR(am.l10n_in_shipping_bill_date, 'DD-MON-YYYY')\n                    ELSE ''\n                    END) as gst_format_shipping_bill_date,\n                CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                    (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_igst', 'tax_report_line_igst_rc'))\n                    THEN aml.balance\n                    ELSE 0\n                    END AS igst_amount,\n                CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                    (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_cgst', 'tax_report_line_cgst_rc'))\n                    THEN aml.balance\n                    ELSE 0\n                    END AS cgst_amount,\n                CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                    (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_sgst', 'tax_report_line_sgst_rc'))\n                    THEN aml.balance\n                    ELSE 0\n                    END AS sgst_amount,\n                (WITH account_tax_temp_table AS (\n                    SELECT account_account_tag_id\n                    FROM account_tax_report_line_tags_rel\n                    WHERE account_tax_report_line_id IN\n                        (SELECT res_id FROM ir_model_data where module='l10n_in' AND name in ('tax_report_line_cess', 'tax_report_line_cess_rc'))\n                    )\n                    SELECT sum(temp_aml.balance) from account_move_line temp_aml\n                    JOIN account_account_tag_account_move_line_rel aat_aml_rel_temp ON aat_aml_rel_temp.account_move_line_id = temp_aml.id\n                    JOIN account_account_tag aat_temp ON aat_temp.id = aat_aml_rel_temp.account_account_tag_id\n                    JOIN account_tax_temp_table tag_rep_ln_temp ON aat_temp.id = tag_rep_ln_temp.account_account_tag_id\n                    where temp_aml.move_id = aml.move_id and temp_aml.product_id = aml.product_id\n                    ) AS cess_amount,\n                CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                    (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_sgst', 'tax_report_line_sgst_rc'))\n                    THEN NULL\n                    ELSE (CASE WHEN aml.tax_base_amount <> 0 THEN aml.tax_base_amount * (CASE WHEN aml.balance < 0 THEN -1 ELSE 1 END) ELSE NULL END)\n                    END AS price_total,\n                (CASE WHEN (aj.type = 'sale' AND am.move_type != 'out_refund') or (aj.type = 'purchase' AND at.l10n_in_reverse_charge AND am.move_type != 'in_refund') THEN -1 ELSE 1 END) AS amount_sign,\n                (CASE WHEN am.move_type in ('in_refund','out_refund')\n                      AND p.vat IS NULL\n                      AND am.l10n_in_gst_treatment != 'overseas'\n                      AND (ABS(am.amount_total_signed) <= 250000 OR\n                          (ps.id = cp.state_id OR p.id IS NULL))\n                      THEN -1\n                      ELSE 1 END) AS b2cs_refund_sign,\n                (CASE WHEN atr.parent_tax IS NOT NULL THEN atr.parent_tax\n                    ELSE at.id END) AS tax_id,\n                (CASE WHEN atr.parent_tax IS NOT NULL THEN parent_at.amount\n                    ELSE at.amount END) AS tax_rate\n        ", kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='sub_select_str', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_from',
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
                            targets=[Name(id='from_str', ctx=Store())],
                            value=Constant(value='\n            FROM account_move_line aml\n                JOIN account_move am ON am.id = aml.move_id\n                JOIN account_journal aj ON aj.id = am.journal_id\n                JOIN res_company c ON c.id = aj.company_id\n                LEFT JOIN account_tax at ON at.id = aml.tax_line_id\n                JOIN account_account_tag_account_move_line_rel aat_aml_rel ON aat_aml_rel.account_move_line_id = aml.id\n                JOIN account_account_tag aat ON aat.id = aat_aml_rel.account_account_tag_id\n                JOIN account_tax_report_line_tags_rel tag_rep_ln ON aat.id = tag_rep_ln.account_account_tag_id\n                LEFT JOIN res_partner cp ON cp.id = COALESCE(aj.l10n_in_gstin_partner_id, c.partner_id)\n                LEFT JOIN res_country_state cps ON cps.id = cp.state_id\n                LEFT JOIN account_move refund_am ON refund_am.id = am.reversed_entry_id\n                LEFT JOIN res_partner p ON p.id = aml.partner_id\n                LEFT JOIN res_country_state ps ON ps.id = am.l10n_in_state_id\n                LEFT JOIN res_partner rp ON rp.id = am.l10n_in_reseller_partner_id\n                LEFT JOIN account_tax_filiation_rel atr ON atr.child_tax = at.id\n                LEFT JOIN account_tax parent_at ON parent_at.id = atr.parent_tax\n                ', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='from_str', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_where',
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
                            value=Constant(value="\n                WHERE am.state = 'posted'\n                    AND tag_rep_ln.account_tax_report_line_id in (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_igst', 'tax_report_line_cgst', 'tax_report_line_sgst', 'tax_report_line_zero_rated', 'tax_report_line_igst_rc', 'tax_report_line_cgst_rc', 'tax_report_line_sgst_rc'))\n        ", kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_group_by',
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
                            targets=[Name(id='group_by_str', ctx=Store())],
                            value=Constant(value='\n        GROUP BY sub.move_id,\n            sub.account_move_id,\n            sub.name,\n            sub.state,\n            sub.partner_id,\n            sub.date,\n            sub.l10n_in_gst_treatment,\n            sub.ecommerce_partner_id,\n            sub.shipping_bill_number,\n            sub.shipping_bill_date,\n            sub.shipping_port_code_id,\n            sub.total,\n            sub.journal_id,\n            sub.company_id,\n            sub.move_type,\n            sub.reversed_entry_id,\n            sub.partner_vat,\n            sub.ecommerce_vat,\n            sub.place_of_supply,\n            sub.is_pre_gst,\n            sub.is_ecommerce,\n            sub.b2cl_is_ecommerce,\n            sub.b2cs_is_ecommerce,\n            sub.supply_type,\n            sub.export_type,\n            sub.refund_export_type,\n            sub.b2b_type,\n            sub.refund_invoice_type,\n            sub.gst_format_date,\n            sub.gst_format_refund_date,\n            sub.gst_format_shipping_bill_date,\n            sub.amount_sign,\n            sub.tax_id,\n            sub.tax_rate,\n            sub.b2cs_refund_sign\n        ', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='group_by_str', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
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
                                    value=Name(id='tools', ctx=Load()),
                                    attr='drop_view_if_exists',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_table',
                                        ctx=Load(),
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
                                    BinOp(
                                        left=Constant(value='CREATE or REPLACE VIEW %s AS (\n            %s\n            FROM (\n                %s %s %s\n            ) AS sub %s)', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_table',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_select',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_sub_select',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_from',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_where',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_group_by',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
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
