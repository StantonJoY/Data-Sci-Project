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
            name='ResCountry',
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
                    value=Constant(value='res.country', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ar_afip_code', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='AFIP Code', kind=None)],
                        keywords=[
                            keyword(
                                arg='size',
                                value=Constant(value=3, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This code will be used on electronic invoice', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ar_natural_vat', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Natural Person VAT', kind=None)],
                        keywords=[
                            keyword(
                                arg='size',
                                value=Constant(value=11, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Generic VAT number defined by AFIP in order to recognize partners from this country that are natural persons', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ar_legal_entity_vat', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Legal Entity VAT', kind=None)],
                        keywords=[
                            keyword(
                                arg='size',
                                value=Constant(value=11, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Generic VAT number defined by AFIP in order to recognize partners from this country that are legal entity', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ar_other_vat', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Other VAT', kind=None)],
                        keywords=[
                            keyword(
                                arg='size',
                                value=Constant(value=11, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Generic VAT number defined by AFIP in order to recognize partners from this country that are not natural persons or legal entities', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)