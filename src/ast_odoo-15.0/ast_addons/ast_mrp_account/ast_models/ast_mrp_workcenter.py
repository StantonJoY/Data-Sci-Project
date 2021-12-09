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
            name='MrpWorkcenter',
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
                    value=Constant(value='mrp.workcenter', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='costs_hour_account_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.analytic.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Analytic Account', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Fill this only if you want automatic analytic accounting entries on production orders.', kind=None),
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
