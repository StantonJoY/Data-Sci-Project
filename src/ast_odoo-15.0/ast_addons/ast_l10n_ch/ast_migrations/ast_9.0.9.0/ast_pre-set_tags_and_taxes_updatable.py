Module(
    body=[
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        FunctionDef(
            name='migrate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='registry', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='registry',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='cr', ctx=Load()),
                                attr='dbname',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                ImportFrom(
                    module='odoo.addons.account.models.chart_template',
                    names=[alias(name='migrate_set_tags_and_taxes_updatable', asname=None)],
                    level=0,
                ),
                Expr(
                    value=Call(
                        func=Name(id='migrate_set_tags_and_taxes_updatable', ctx=Load()),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='registry', ctx=Load()),
                            Constant(value='l10n_ch', kind=None),
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
    type_ignores=[],
)
