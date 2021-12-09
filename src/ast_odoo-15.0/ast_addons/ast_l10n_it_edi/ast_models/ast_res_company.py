Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='TAX_SYSTEM', ctx=Store())],
            value=List(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='RF01', kind=None),
                            Constant(value='[RF01] Ordinario', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF02', kind=None),
                            Constant(value='[RF02] Contribuenti minimi (art.1, c.96-117, L. 244/07)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF04', kind=None),
                            Constant(value='[RF04] Agricoltura e attività connesse e pesca (artt.34 e 34-bis, DPR 633/72)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF05', kind=None),
                            Constant(value='[RF05] Vendita sali e tabacchi (art.74, c.1, DPR. 633/72)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF06', kind=None),
                            Constant(value='[RF06] Commercio fiammiferi (art.74, c.1, DPR  633/72)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF07', kind=None),
                            Constant(value='[RF07] Editoria (art.74, c.1, DPR  633/72)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF08', kind=None),
                            Constant(value='[RF08] Gestione servizi telefonia pubblica (art.74, c.1, DPR 633/72)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF09', kind=None),
                            Constant(value='[RF09] Rivendita documenti di trasporto pubblico e di sosta (art.74, c.1, DPR  633/72)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF10', kind=None),
                            Constant(value='[RF10] Intrattenimenti, giochi e altre attività di cui alla tariffa allegata al DPR 640/72 (art.74, c.6, DPR 633/72)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF11', kind=None),
                            Constant(value='[RF11] Agenzie viaggi e turismo (art.74-ter, DPR 633/72)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF12', kind=None),
                            Constant(value='[RF12] Agriturismo (art.5, c.2, L. 413/91)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF13', kind=None),
                            Constant(value='[RF13] Vendite a domicilio (art.25-bis, c.6, DPR  600/73)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF14', kind=None),
                            Constant(value='[RF14] Rivendita beni usati, oggetti d’arte, d’antiquariato o da collezione (art.36, DL 41/95)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF15', kind=None),
                            Constant(value='[RF15] Agenzie di vendite all’asta di oggetti d’arte, antiquariato o da collezione (art.40-bis, DL 41/95)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF16', kind=None),
                            Constant(value='[RF16] IVA per cassa P.A. (art.6, c.5, DPR 633/72)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF17', kind=None),
                            Constant(value='[RF17] IVA per cassa (art. 32-bis, DL 83/2012)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF18', kind=None),
                            Constant(value='[RF18] Altro', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='RF19', kind=None),
                            Constant(value='[RF19] Regime forfettario (art.1, c.54-89, L. 190/2014)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ResCompany',
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
                    value=Constant(value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_codice_fiscale', ctx=Store())],
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
                                value=Constant(value='Codice Fiscale', kind=None),
                            ),
                            keyword(
                                arg='size',
                                value=Constant(value=16, kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='partner_id.l10n_it_codice_fiscale', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Fiscal code of your company', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_tax_system', ctx=Store())],
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
                                value=Name(id='TAX_SYSTEM', ctx=Load()),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Tax System', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Please select the Tax system to which you are subjected.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_mail_pec_server_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.mail_server', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Server PEC', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Configure your PEC-mail server to send electronic invoices.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_address_recipient_fatturapa', ctx=Store())],
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
                                value=Constant(value='Government PEC-mail', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Enter Government PEC-mail address. Ex: sdi01@pec.fatturapa.it', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_address_send_fatturapa', ctx=Store())],
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
                                value=Constant(value='Company PEC-mail', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Enter your company PEC-mail address. Ex: yourcompany@pec.mail.it', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_has_eco_index', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The seller/provider is a company listed on the register of companies and as        such must also indicate the registration data on all documents (art. 2250, Italian        Civil Code)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_eco_index_office', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.country.state', kind=None)],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Constant(value="[('country_id','=','IT')]", kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Province of the register-of-companies office', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_eco_index_number', ctx=Store())],
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
                                value=Constant(value='Number in register of companies', kind=None),
                            ),
                            keyword(
                                arg='size',
                                value=Constant(value=20, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field must contain the number under which the        seller/provider is listed on the register of companies.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_eco_index_share_capital', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Share capital actually paid up', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Mandatory if the seller/provider is a company with share        capital (SpA, SApA, Srl), this field must contain the amount        of share capital actually paid up as resulting from the last        financial statement', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_eco_index_sole_shareholder', ctx=Store())],
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
                                            Constant(value='NO', kind=None),
                                            Constant(value='Not a limited liability company', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='SU', kind=None),
                                            Constant(value='Socio unico', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='SM', kind=None),
                                            Constant(value='Più soci', kind=None),
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
                                value=Constant(value='Shareholder', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_eco_index_liquidation_state', ctx=Store())],
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
                                            Constant(value='LS', kind=None),
                                            Constant(value='The company is in a state of liquidation', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='LN', kind=None),
                                            Constant(value='The company is not in a state of liquidation', kind=None),
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
                                value=Constant(value='Liquidation state', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_has_tax_representative', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The seller/provider is a non-resident subject which        carries out transactions in Italy with relevance for VAT        purposes and which takes avail of a tax representative in        Italy', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_tax_representative_partner_id', ctx=Store())],
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
                                value=Constant(value='Tax representative partner', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_eco_admin_index',
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
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='l10n_it_has_eco_index',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='l10n_it_eco_index_office',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='l10n_it_eco_index_number',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='l10n_it_eco_index_share_capital',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='l10n_it_eco_index_sole_shareholder',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='l10n_it_eco_index_liquidation_state',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='All fields about the Economic and Administrative Index must be completed.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
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
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='l10n_it_has_eco_index', kind=None),
                                Constant(value='l10n_it_eco_index_office', kind=None),
                                Constant(value='l10n_it_eco_index_number', kind=None),
                                Constant(value='l10n_it_eco_index_share_capital', kind=None),
                                Constant(value='l10n_it_eco_index_sole_shareholder', kind=None),
                                Constant(value='l10n_it_eco_index_liquidation_state', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_tax_representative',
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
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='l10n_it_has_tax_representative',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='l10n_it_tax_representative_partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You must select a tax representative.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='l10n_it_tax_representative_partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='vat',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Your tax representative partner must have a tax number.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='l10n_it_tax_representative_partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Your tax representative partner must have a country.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
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
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='l10n_it_has_tax_representative', kind=None),
                                Constant(value='l10n_it_tax_representative_partner_id', kind=None),
                            ],
                            keywords=[],
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
