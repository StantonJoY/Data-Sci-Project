Module(
    body=[
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='TransactionCase', asname=None),
                alias(name='tagged', asname=None),
                alias(name='TagsSelector', asname=None),
                alias(name='BaseCase', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestSetTags',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_set_tags_empty',
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
                            value=Constant(value='Test the set_tags decorator with an empty set of tags', kind=None),
                        ),
                        ClassDef(
                            name='FakeClass',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='fc', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeClass', ctx=Load()),
                                args=[],
                                keywords=[],
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
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='fc', ctx=Load()),
                                            Constant(value='test_tags', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_tags',
                                        ctx=Load(),
                                    ),
                                    Set(
                                        elts=[
                                            Constant(value='at_install', kind=None),
                                            Constant(value='standard', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_module',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base', kind=None),
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
                    name='test_set_tags_not_decorated',
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
                            value=Constant(value='Test that a TransactionCase has some test_tags by default', kind=None),
                        ),
                        ClassDef(
                            name='FakeClass',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[],
                        ),
                        Assign(
                            targets=[Name(id='fc', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeClass', ctx=Load()),
                                args=[],
                                keywords=[],
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
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='fc', ctx=Load()),
                                            Constant(value='test_tags', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_tags',
                                        ctx=Load(),
                                    ),
                                    Set(
                                        elts=[
                                            Constant(value='at_install', kind=None),
                                            Constant(value='standard', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_module',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base', kind=None),
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
                    name='test_set_tags_single_tag',
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
                            value=Constant(value='Test the set_tags decorator with a single tag', kind=None),
                        ),
                        ClassDef(
                            name='FakeClass',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[Constant(value='slow', kind=None)],
                                    keywords=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='fc', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeClass', ctx=Load()),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_tags',
                                        ctx=Load(),
                                    ),
                                    Set(
                                        elts=[
                                            Constant(value='at_install', kind=None),
                                            Constant(value='standard', kind=None),
                                            Constant(value='slow', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_module',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base', kind=None),
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
                    name='test_set_tags_multiple_tags',
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
                            value=Constant(value='Test the set_tags decorator with multiple tags', kind=None),
                        ),
                        ClassDef(
                            name='FakeClass',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[
                                        Constant(value='slow', kind=None),
                                        Constant(value='nightly', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='fc', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeClass', ctx=Load()),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_tags',
                                        ctx=Load(),
                                    ),
                                    Set(
                                        elts=[
                                            Constant(value='at_install', kind=None),
                                            Constant(value='standard', kind=None),
                                            Constant(value='slow', kind=None),
                                            Constant(value='nightly', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_module',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base', kind=None),
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
                    name='test_inheritance',
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
                            value=Constant(value="Test inheritance when using the 'tagged' decorator", kind=None),
                        ),
                        ClassDef(
                            name='FakeClassA',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[Constant(value='slow', kind=None)],
                                    keywords=[],
                                ),
                            ],
                        ),
                        ClassDef(
                            name='FakeClassB',
                            bases=[Name(id='FakeClassA', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[Constant(value='nightly', kind=None)],
                                    keywords=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='fc', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeClassB', ctx=Load()),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_tags',
                                        ctx=Load(),
                                    ),
                                    Set(
                                        elts=[
                                            Constant(value='at_install', kind=None),
                                            Constant(value='standard', kind=None),
                                            Constant(value='nightly', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_module',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        ClassDef(
                            name='FakeClassC',
                            bases=[Name(id='FakeClassA', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[],
                        ),
                        Assign(
                            targets=[Name(id='fc', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeClassC', ctx=Load()),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_tags',
                                        ctx=Load(),
                                    ),
                                    Set(
                                        elts=[
                                            Constant(value='at_install', kind=None),
                                            Constant(value='standard', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_module',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base', kind=None),
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
                    name='test_untagging',
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
                            value=Constant(value="Test that one can remove the 'standard' tag", kind=None),
                        ),
                        ClassDef(
                            name='FakeClassA',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[Constant(value='-standard', kind=None)],
                                    keywords=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='fc', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeClassA', ctx=Load()),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_tags',
                                        ctx=Load(),
                                    ),
                                    Set(
                                        elts=[Constant(value='at_install', kind=None)],
                                    ),
                                ],
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
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_module',
                                        ctx=Load(),
                                    ),
                                    Constant(value='base', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        ClassDef(
                            name='FakeClassB',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[
                                        Constant(value='-standard', kind=None),
                                        Constant(value='-base', kind=None),
                                        Constant(value='-at_install', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='fc', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeClassB', ctx=Load()),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_tags',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        ClassDef(
                            name='FakeClassC',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[
                                        Constant(value='-standard', kind=None),
                                        Constant(value='-base', kind=None),
                                        Constant(value='-at_install', kind=None),
                                        Constant(value='fast', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='fc', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeClassC', ctx=Load()),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='fc', ctx=Load()),
                                        attr='test_tags',
                                        ctx=Load(),
                                    ),
                                    Set(
                                        elts=[Constant(value='fast', kind=None)],
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='nodatabase', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestSelector',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_selector_parser',
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
                            value=Constant(value='Test the parser part of the TagsSelector class', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+slow', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='slow', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+slow,nightly', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='slow', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='nightly', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+slow,-standard', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='slow', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+slow, -standard', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='slow', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+slow , -standard', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='slow', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+slow ,-standard,+js', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='slow', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='js', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow, ', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='slow', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+slow,-standard, slow,-standard ', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='slow', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='', kind=None)],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='/module', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='*/module', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value=':class', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value='class', kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='.method', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value='method', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value=':class.method', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value='class', kind=None),
                                                    Constant(value='method', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='/module:class.method', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value='class', kind=None),
                                                    Constant(value='method', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='*/module:class.method', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value='class', kind=None),
                                                    Constant(value='method', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-/module:class.method', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value='class', kind=None),
                                                    Constant(value='method', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-*/module:class.method', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value='class', kind=None),
                                                    Constant(value='method', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='tag/module', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='tag', kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='tag.method', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='tag', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value='method', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='*/module,-standard', kind=None)],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='include',
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Set(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='standard', kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='tags', ctx=Load()),
                                        attr='exclude',
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='nodatabase', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestSelectorSelection',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_selector_selection',
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
                            value=Constant(value='Test check_tags use cases', kind=None),
                        ),
                        ClassDef(
                            name='Test_A',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[],
                        ),
                        ClassDef(
                            name='Test_B',
                            bases=[Name(id='BaseCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[Constant(value='stock', kind=None)],
                                    keywords=[],
                                ),
                            ],
                        ),
                        ClassDef(
                            name='Test_C',
                            bases=[Name(id='BaseCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[
                                        Constant(value='stock', kind=None),
                                        Constant(value='slow', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ],
                        ),
                        ClassDef(
                            name='Test_D',
                            bases=[Name(id='BaseCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[
                                        Constant(value='standard', kind=None),
                                        Constant(value='slow', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ],
                        ),
                        ClassDef(
                            name='Test_E',
                            bases=[Name(id='TransactionCase', ctx=Load())],
                            keywords=[],
                            body=[Pass()],
                            decorator_list=[
                                Call(
                                    func=Name(id='tagged', ctx=Load()),
                                    args=[
                                        Constant(value='-at_install', kind=None),
                                        Constant(value='post_install', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='no_tags_obj', ctx=Store())],
                            value=Call(
                                func=Name(id='Test_A', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stock_tag_obj', ctx=Store())],
                            value=Call(
                                func=Name(id='Test_B', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='multiple_tags_obj', ctx=Store())],
                            value=Call(
                                func=Name(id='Test_C', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='multiple_tags_standard_obj', ctx=Store())],
                            value=Call(
                                func=Name(id='Test_D', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='post_install_obj', ctx=Store())],
                            value=Call(
                                func=Name(id='Test_E', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='no_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+slow', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='no_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+slow,fake', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='no_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow,standard', kind=None)],
                                keywords=[],
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
                                args=[Name(id='no_tags_obj', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow,-standard', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='no_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-slow,-standard', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='no_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-slow,+standard', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='no_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stock_tag_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stock_tag_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='standard', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stock_tag_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow,standard', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stock_tag_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow,-standard', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stock_tag_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='+stock', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stock_tag_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='stock,fake', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stock_tag_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='stock,standard', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stock_tag_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-stock', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stock_tag_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-stock', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-slow', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow,stock', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-slow,stock', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow,stock,-slow', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_standard_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='standard', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_standard_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_standard_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow,fake', kind=None)],
                                keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_standard_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-slow', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_standard_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-standard', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_standard_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='-slow,-standard', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_standard_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='standard,-slow', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_standard_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='slow,-standard', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tags', ctx=Load()),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='multiple_tags_standard_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='standard', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='position', ctx=Store())],
                            value=Call(
                                func=Name(id='TagsSelector', ctx=Load()),
                                args=[Constant(value='post_install', kind=None)],
                                keywords=[],
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
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tags', ctx=Load()),
                                                    attr='check',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='post_install_obj', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='position', ctx=Load()),
                                                    attr='check',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='post_install_obj', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='nodatabase', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
