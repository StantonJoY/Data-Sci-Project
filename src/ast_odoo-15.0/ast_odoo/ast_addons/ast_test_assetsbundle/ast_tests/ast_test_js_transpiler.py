Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='transpile_javascript', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestJsTranspiler',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='maxDiff', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_01_alias',
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
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='/** @odoo-module alias=test_assetsbundle.Alias **/', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/alias.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='odoo.define(\'@test_assetsbundle/alias\', async function (require) {\n\'use strict\';\nlet __exports = {};\n/** @odoo-module alias=test_assetsbundle.Alias **/\nreturn __exports;\n});\n\nodoo.define(`test_assetsbundle.Alias`, async function(require) {\n                        return require(\'@test_assetsbundle/alias\')[Symbol.for("default")];\n                        });\n', kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_02_default',
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
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='/** @odoo-module alias=test_assetsbundle.Alias default=False **/', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/alias.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value="odoo.define('@test_assetsbundle/alias', async function (require) {\n'use strict';\nlet __exports = {};\n/** @odoo-module alias=test_assetsbundle.Alias default=False **/\nreturn __exports;\n});\n\nodoo.define(`test_assetsbundle.Alias`, async function(require) {\n                        return require('@test_assetsbundle/alias');\n                        });\n", kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='/** @odoo-module alias=test_assetsbundle.Alias default=0 **/', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/alias.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value="odoo.define('@test_assetsbundle/alias', async function (require) {\n'use strict';\nlet __exports = {};\n/** @odoo-module alias=test_assetsbundle.Alias default=0 **/\nreturn __exports;\n});\n\nodoo.define(`test_assetsbundle.Alias`, async function(require) {\n                        return require('@test_assetsbundle/alias');\n                        });\n", kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='/** @odoo-module alias=test_assetsbundle.Alias default=false **/', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/alias.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value="odoo.define('@test_assetsbundle/alias', async function (require) {\n'use strict';\nlet __exports = {};\n/** @odoo-module alias=test_assetsbundle.Alias default=false **/\nreturn __exports;\n});\n\nodoo.define(`test_assetsbundle.Alias`, async function(require) {\n                        return require('@test_assetsbundle/alias');\n                        });\n", kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_03_classes',
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
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='export default class Nice {}\n\nclass Vehicule {}\n\nexport class Car extends Vehicule {}\n\nexport class Boat extends Vehicule {}\n\nexport const Ferrari = class Ferrari extends Car {};\n', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/classes.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='odoo.define(\'@test_assetsbundle/classes\', async function (require) {\n\'use strict\';\nlet __exports = {};\nconst Nice = __exports[Symbol.for("default")] = class Nice {}\n\nclass Vehicule {}\n\nconst Car = __exports.Car = class Car extends Vehicule {}\n\nconst Boat = __exports.Boat = class Boat extends Vehicule {}\n\nconst Ferrari = __exports.Ferrari = class Ferrari extends Car {};\n\nreturn __exports;\n});\n', kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_04_comments',
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
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='/**\n * This is a comment\n */\n\n/**\n * This isn\'t a string\n */\nexport class Test {\n  // This is a comment in a class\n}\n\n/* cool comment */ const a = 5; /* another cool comment */\n\nconst b = 5; // hello\n\n// another one\n\nconst y = "this is a /* nice string and should be kept */";\nconst z = "this is a /* nice string and should be kept";\nexport const x = "this is a // nice string and should be kept";\nconst w = "this is a */ nice string and should be kept";\n\n// This isn\'t a string\n/*\n  comments\n */\nconst aaa = "keep!";\n/*\n  comments\n */\n', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/comments.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='odoo.define(\'@test_assetsbundle/comments\', async function (require) {\n\'use strict\';\nlet __exports = {};\n/**\n * This is a comment\n */\n\n/**\n * This isn\'t a string\n */\nconst Test = __exports.Test = class Test {\n  // This is a comment in a class\n}\n\n/* cool comment */ const a = 5; /* another cool comment */\n\nconst b = 5; // hello\n\n// another one\n\nconst y = "this is a /* nice string and should be kept */";\nconst z = "this is a /* nice string and should be kept";\nconst x = __exports.x = "this is a // nice string and should be kept";\nconst w = "this is a */ nice string and should be kept";\n\n// This isn\'t a string\n/*\n  comments\n */\nconst aaa = "keep!";\n/*\n  comments\n */\n\nreturn __exports;\n});\n', kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_05_functions',
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
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='export function sayHello() {\n  console.log("Hello");\n}\n\nexport function sayHelloWorld() {\n  console.log("Hello world");\n}\n\nexport async function sayAsyncHello() {\n  console.log("Hello Async");\n}\n\n\nexport default function sayHelloDefault() {\n  console.log("Hello Default");\n}\n', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/functions.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='odoo.define(\'@test_assetsbundle/functions\', async function (require) {\n\'use strict\';\nlet __exports = {};\nconst sayHello = __exports.sayHello = function sayHello() {\n  console.log("Hello");\n}\n\nconst sayHelloWorld = __exports.sayHelloWorld = function sayHelloWorld() {\n  console.log("Hello world");\n}\n\nconst sayAsyncHello = __exports.sayAsyncHello = async function sayAsyncHello() {\n  console.log("Hello Async");\n}\n\n\nconst sayHelloDefault = __exports[Symbol.for("default")] = function sayHelloDefault() {\n  console.log("Hello Default");\n}\n\nreturn __exports;\n});\n', kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_06_import',
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
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='/**\n * import { Dialog, Notification } from "../src/Dialog";\n */\nimport { Line1 } from "../src/Dialog";\nimport { Line2, Notification } from "../src/Dialog";\nimport { Line3, Notification } from "Dialog";\nimport { Line4, Notification } from "@tests/Dialog";\nimport { Line5, Notification } from "./Dialog";\nimport { Line6, Notification } from \'../src/Dialog\'\nimport Line7  from "../src/Dialog";\nimport  Line8  from \'../src/Dialog\';\n\nimport Line9  from "test.Dialog";\nimport  { Line10, Notification }  from \'test.Dialog2\';\n\nimport * as Line11 from "test.Dialog";\nimport "test.Dialog";\n\nimport Line12  from "@test.Dialog"; //HELLO\nimport {Line13}  from "@test.Dialog" //HELLO\n\n\nconst test = `import { Line14, Notification } from "../src/Dialog";`\n\nimport Line15 from "test/Dialog";\nimport Line16 from "test.Dialog.error";\n', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/import.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='odoo.define(\'@test_assetsbundle/import\', async function (require) {\n\'use strict\';\nlet __exports = {};\n/**\n * import { Dialog, Notification } from "../src/Dialog";\n */\nconst { Line1 } = require("@test_assetsbundle/Dialog");\nconst { Line2, Notification } = require("@test_assetsbundle/Dialog");\nconst { Line3, Notification } = require("Dialog");\nconst { Line4, Notification } = require("@tests/Dialog");\nconst { Line5, Notification } = require("@test_assetsbundle/Dialog");\nconst { Line6, Notification } = require("@test_assetsbundle/Dialog")\nconst Line7 = require("@test_assetsbundle/Dialog")[Symbol.for("default")];\nconst Line8 = require("@test_assetsbundle/Dialog")[Symbol.for("default")];\n\nconst Line9 = require("test.Dialog");\nconst { Line10, Notification } = require(\'test.Dialog2\');\n\nconst Line11 = require("test.Dialog");\nrequire("test.Dialog");\n\nconst Line12 = require("@test.Dialog")[Symbol.for("default")]; //HELLO\nconst {Line13} = require("@test.Dialog") //HELLO\n\n\nconst test = `import { Line14, Notification } from "../src/Dialog";`\n\nconst Line15 = require("test/Dialog");\nconst Line16 = require("test.Dialog.error");\n\nreturn __exports;\n});\n', kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_07_index',
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
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='export const a = 5;\n\nimport * as b from "@tests/dir";\n\nimport c from "@tests/dir/index/";\n\nimport d from "@tests";', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/index.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='odoo.define(\'@test_assetsbundle\', async function (require) {\n\'use strict\';\nlet __exports = {};\nconst a = __exports.a = 5;\n\nconst b = require("@tests/dir");\n\nconst c = require("@tests/dir")[Symbol.for("default")];\n\nconst d = require("@tests")[Symbol.for("default")];\nreturn __exports;\n});\n', kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_08_list',
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
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='export {a, b};\n\nexport {a as aa, b, c as cc};\nexport {a, aReallyVeryLongNameWithSomeExtra}\nexport {\n        a,\n        aReallyVeryLongNameWithSomeExtra,\n        }\nexport {\n        a,\n        aReallyVeryLongNameWithSomeExtra\n        }\n\n\nexport {a, aReallyVeryLongNameWithSomeExtra /* a comment must not cause catastrophic backtracking, even if not supported */};\n\nexport {c, d} from "@tests/Dialog";\nexport {e} from "../src/Dialog";\n\nexport {c as cc, d, e as ee} from "@tests/Dialog";\n\nexport * from "@tests/Dialog";\n', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/list.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='odoo.define(\'@test_assetsbundle/list\', async function (require) {\n\'use strict\';\nlet __exports = {};\nObject.assign(__exports, {a,  b});\n\nObject.assign(__exports, {aa: a,  b, cc:  c});\nObject.assign(__exports, {a,  aReallyVeryLongNameWithSomeExtra})\nObject.assign(__exports, {\n        a, \n        aReallyVeryLongNameWithSomeExtra, \n        })\nObject.assign(__exports, {\n        a, \n        aReallyVeryLongNameWithSomeExtra\n        })\n\n\nexport {a, aReallyVeryLongNameWithSomeExtra /* a comment must not cause catastrophic backtracking, even if not supported */};\n\n{const {c, d} = require("@tests/Dialog");Object.assign(__exports, {c,  d})};\n{const {e} = require("@test_assetsbundle/Dialog");Object.assign(__exports, {e})};\n\n{const {c, d, e} = require("@tests/Dialog");Object.assign(__exports, {cc: c,  d, ee:  e})};\n\nObject.assign(__exports, require("@tests/Dialog"));\n\nreturn __exports;\n});\n', kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_09_variables',
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
                            targets=[Name(id='input_content', ctx=Store())],
                            value=Constant(value='export const v = 5;\n\nconst a = 12;\nconst b = 15;\n\nexport { a, b };\n\nexport default 100;\n\nexport default a;\n', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='transpile_javascript', ctx=Load()),
                                args=[
                                    Constant(value='/test_assetsbundle/static/src/variables.js', kind=None),
                                    Name(id='input_content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='odoo.define(\'@test_assetsbundle/variables\', async function (require) {\n\'use strict\';\nlet __exports = {};\nconst v = __exports.v = 5;\n\nconst a = 12;\nconst b = 15;\n\nObject.assign(__exports, { a,  b });\n\n__exports[Symbol.for("default")] = 100;\n\n__exports[Symbol.for("default")] = a;\n\nreturn __exports;\n});\n', kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expected_result', ctx=Load()),
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
                    args=[
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
